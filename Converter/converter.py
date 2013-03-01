# -*- coding: utf-8 -*-

"""
This script converts data from files which have been created by moSINS software or
test4converter.py script into text file. Indeed script provides to user choice
which data he or she can convert. Converted data save into text file.
"""

import glob
import struct
from operator import add
from soft4recieve_write_Rel2.set_working_path import in_path, test_path, com_path
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
#    first_line = raw_file.readline()[:-1] #replace \n symbol
    first_line = raw_file.readline(1100) #replace \n symbol
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
    buf, new_pack, buf1 = [], [], []
    group_buf = packets[0]['group']
    for p in packets:
        p['bin'] = first_line[p['shift']*2:p['shift']*2 + p['size']*2]
        buf.append(p) # accumulate data for one group
        if group_buf != p['group']: # detecting groups changing
            group_buf = p['group']
            buf1.append(buf.pop(-1))# last packet in buf is belonged to next group. moves it to buf1
            sub_line = ''.join([i['bin'] for i in buf])
            if len(''.join(sub_line.split('23'))): # Choose the source groups which
                new_pack += [p for p in buf if p['cut_name']] # don't contain symbol '#'(23)
                buf = buf1
            else:
                buf = buf1
            buf1 = []
    return new_pack + buf

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
        # Initialasing of buffer by adding order numbers of KKP's second and count
        name = lambda name:[p for p in in_data if p['cut_name'] == name]
        buf = name('Sec') + name('Count')
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

def line_from_file(file_dict):
    """
    Function extract rows, row's and file's ordering numbers from files of
    file_dicts
    """
    for files in enumerate(sorted(file_dict)):# Open binary files for reading
        for lines in enumerate(open(file_dict[files[1]],'r')):
            yield (files[0],lines[0],lines[1])

def main_fun(sfd,nfp,**args):
    """
    Function extract data from bin files according to user_data structure.

    Keyword arguments:
    user_data - list of dictionaries of available data for extracting.
    """
    for args['file'], args['row'], args['line'] in line_from_file(sfd):#read data from files
        for func in nfp.values():
            try:
                # Create file's object from function's attribute that stores path to writing file
                func_file = open(func['path']%args.my_file,'a')
                func_file.write(func['func'](**args))
                func_file.close()
            except AttributeError:
                # Create file, write head string and first line
                func_file = open(func['path']%args,'w')
                func_file.write('This is head of %s\n\n'%func['func'].__name__)
                func_file.write(func['func'](**args))
                func_file.close()
                # Attach file's name as function attribute
                func['func'].__setattr__('my_file' ,func['func'].__name__ + func['path'])

def edit_func_pool(avail_data):
    """
    Function create copy of func_pool structure from set_working_file and replace
    inside it names of source groups which are not in avail_data.
    """
    from soft4recieve_write_Rel2.Converter.mapping_functions import func_pool
    # Get names of source groups
    groups_name = set([i['group'].split('_')[0] for i in avail_data if i.has_key('group')])
    nfp = copy.deepcopy(func_pool)
    # Get list of group's key from nfp
    for key, val in nfp.items():
        if val.has_key('group'):
            if val['group'] not in groups_name:
                nfp.pop(key)
            elif val.has_key('quest'):
                if raw_input(val['quest']) == 'n':
                    nfp.pop(key)
    print groups_name
    return nfp

# Get dictionary of binary files
sort_file_dict = lambda path:sort_files(glob.glob(path + '*.dat'),'bin')
# Get date and time from full_name
date_from_bin_file = lambda f_name:f_name[10:]

if __name__ == "__main__":
    from mapping_functions import glob_args as args
    # ====== Preparing data for converting ======
    # Get dictionary of binary files
    sfd = sort_file_dict(in_path)
    # Get list of available data
    new_packets = get_available_data(sfd)
    # Show list of available data
    show_available_data(new_packets)
    # Get user data
    user_data = get_user_data(new_packets)
    # Edit func_pool depending on user_data
    new_fp = edit_func_pool(user_data)
    # ====== Initial keys for glob_args =======
    # Set short file name
    args['1st_f_name'] = sfd[min(sfd)][-30:-4]
    # Set date and time from full_name
    args['file_date'] = date_from_bin_file(args['1st_f_name'])
    # Set names of data groups
    args['group_name'] = user_group_name2str(user_data)
    # Set user_data as argument
    args['user_data'] = user_data
    # Call main_fun function
    main_fun(sfd,new_fp,**args)