# -*- coding: utf-8 -*-

"""
This script converts data from files which have been created by moSINS software or
test4converter.py script into text file. Indeed script provides to user choice
which data he or she can convert. Converted data save into text file.
"""

import glob
import struct
from operator import add
from soft4recieve_write_Rel2.set_working_path import conv_data,test_data
from soft4recieve_write_Rel2.main_lib import *
from soft4recieve_write_Rel2.moSINS.lib4kkp.lib4kkp import extract_kkp_frame_cell
from soft4recieve_write_Rel2.moSINS.lib4sns.lib4sns import extract_sns_time
from soft4recieve_write_Rel2.data_structure import packets

#==============================================================================
# First we have to find out which data source groups are in binary file. For
# this we read first line from first binary file, search substrings which
# contain symbol '#' (h23) snd exclude groups from all_data dictionary which
# contain this symbol.

#==============================================================================

def get_first_line(file_dict):
    """
    Function extract and return first line from the first file in file_dict.
    """
    first_file = min(file_dict)
    raw_file = open(file_dict[first_file],'r')
    first_line = raw_file.readline()[:-1] #replace \n symbol
    raw_file.close()
    if sum([i['size'] for i in packets])*2 == len(first_line):
        return first_line
    else:
        print 'Invalid length of file\'s string!%s' % len(first_line)
        return None

def get_available_data(file_dict):
    """
    Define groups of sources (SNS,KNS,IMU,ODO,SINS) which data has been written
    to raw files.

    Keyword arguments:
    file_dict -- dictionary which contains working path.
    buf -- list of dictionaries which contain information about data for
    converting.
    """
    first_line = get_first_line(file_dict)
    buf = []
    # Choose the source groups which don't contain symbol '#'(23)
    for p in packets:
        p['bin'] = first_line[p['shift']*2:p['shift']*2 + p['size']*2]
        if ''.join(p['bin'].split('23')) != '':
            if p['cut_name']:# add only 'main' packets
                buf.append(p)
    return (buf)

def show_available_data(in_data):
    """
    This function offers to user list of available data for converting.
    """
    print '=============================================='
    print u'Доступные источники данных для восстановления:'
    for pos_pack in enumerate(in_data):
        pos, pack = pos_pack[0], pos_pack[1]
        if pack['cut_name']:
            if pack['group'] == 'IMU' and pack['cut_name'][0] == 'd':# filter Sec, Frame/Count name
                print '%s:\t%s\t(%d)' % (pack['group'], pack['name'], pos)
            elif pack['group'] != 'IMU':
                print '%s:\t%s\t(%d)' % (pack['group'], pack['name'], pos)
    print '=============================================='

def get_user_data(in_data):
    """
    Function get in_data list of available data and return list of parameters
    chosen by user.
    """
    user_data = raw_input('Input list of values for converting: ')
    try:
        buf = []
        user_in = map(int,user_data.split(','))
        if set(user_in).issubset(set(range(len(in_data)))):
            for item in enumerate(in_data):
                if item[0] in user_in:
                    buf.append(in_data[item[0]])
            return buf
        else:
            print 'You have input wrong data!'
            return []
    except:
        print 'You have input wrong data again!'
        return []

def wrap4files(file_dict, packets, usr_fun, usr_file):
    """
    Function extract line from file from file group and pass it to particular
    function for father mapping.

    Keyword arguments:
    file_dict -- dictionary which contains names of working files'
    usr_fun -- user function
    """
    for files in enumerate(sorted(file_dict)):# Open binary files for reading
        file_num = files[0]
        raw_file = open(file_dict[files[1]],'r')
        for lines in enumerate(raw_file):
            line_num, line = lines[0], lines[1]
            data2file = usr_fun(packets,line,file_num,line_num)
            usr_file.write(''.join(data2file)[:-1])# replace last separator
        raw_file.close()
    usr_file.close()

def extract_data(usr_packets,hex_line,sep):
    """
    Function extracts chosen data from hexadecimal string line and returns
    their as formatted string.
    """
    buf = []
    for p in usr_packets:
        hex_val = hex_line[p['shift']*2:p['shift']*2 + p['size']*2]
        dec_val = struct.unpack(p['BOM'] + p['type'], hex_val.decode('hex'))[0]
        if p['cut_name'] == 'Frame/Count': # extract KKP's frame and cell
            frame, cell = extract_kkp_frame_cell(dec_val)
            buf.append(format_data(frame,sep))
            buf.append(format_data(cell,sep))
        elif p['cut_name'] == 'Tm_SNS':# extract sns time
            tm_sns = extract_sns_time(bit_inversion(hex_val))
            buf.append(format_data(tm_sns,sep))
        else:
            buf.append(format_data(dec_val,sep))
    return buf

def user_group_name2str(user_data):
    """
    Function combines string of group's names in user_data list.
    """
    try:
        return ''.join(set([name['group'] + '_' for name in user_data]))
    except:
        print "Problem in user_group_name2str function!"

def line_from_file(file_dict):
    """
    Function extract rows, row's and file's ordering numbers from files of
    file_dicts
    """
    for files in enumerate(sorted(file_dict)):# Open binary files for reading
        for lines in enumerate(open(file_dict[files[1]],'r')):
            yield (files[1],lines[0],lines[1])

def main_fun(file_dict,**funlist):
    """
    Function extract data from bin files according to user_data structure.

    Keyword arguments:
    user_data - list of dictionaries of available data for extracting.
    """

    for files in enumerate(sorted(file_dict)):# Open binary files for reading
        for lines in enumerate(open(file_dict[files[1]],'r')):
            pass

if __name__ == "__main__":
    # Create list of files for converting
    file_list = glob.glob(get_path(test_data)['common'] + '*.dat')
    # Create dictionary of binary files for converting
    file_dict = sort_files(file_list,'bin')
    # Get first file's name
    full_name = file_dict[sorted(file_dict)[0]]
    print "First file's name: \n", full_name
    # Get date and time from full_name
    date_from_bin_file = full_name.split('\\')[-1][10:-4]
    print "Date and time: ", date_from_bin_file

#    for key in sorted(file_dict):
#        print file_dict[key]
#    print
    # Get list of available data
#    new_packets = get_available_data(file_dict)
    # Show list of available data
#    show_available_data(new_packets)
    # Get user data
#    user_data = get_user_data(new_packets)
#    head2file(get_path4file(conv_data,'out_main','main_test.dat','w'),user_data)
#    result = extract_data(user_data,get_first_line(file_dict),'\t')
    #====================================
    # Main loop
#    for fun in range(4):
#        (file_num,line_num,rawline) = line_from_file(file_dict)
#        print
    # Create generator for extracting rows, row's and file's ordering numbers from files
#    complex_data = ((files[1],lines[0],lines[1]) for files in enumerate(sorted(file_dict))
#         for lines in enumerate(open(file_dict[files[1]],'r')))
#    sd = line_from_file(file_dict)
#    print next(sd)
#    print next(sd)
#    print next(sd)
#    print next(sd)
#    f1 = lambda x: x+2
#    f1(3)
