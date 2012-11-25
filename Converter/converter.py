# -*- coding: utf-8 -*-

"""
This script converts data from files which have been created by moSINS software or
test4converter.py script into text file. Indeed script provides to user choice
which data he or she can convert. Converted data save into text file.
"""

import glob
import re
from operator import add
from set_working_path import conv_data
from main_lib import *
from data_structure import packets

#==============================================================================
# First we have to find out which data source groups are in binary file. For
# this we read first line from first binary file, search substrings which
# contain symbol '#' (h23) snd exclude groups from all_data dictionary which
# contain this symbol.

#==============================================================================
# Create list of files for converting
file_list = glob.glob(get_path(conv_data)['in1'] + '*.dat')
# Create dictionary of binary files for converting
file_dict = sort_files(file_list,'bin')

def get_first_line(file_dict):
    """
    Function extract and return first line from the first file in file_dict.
    """
    first_file = min(file_dict)
    raw_file = open(file_dict[first_file],'r')
    first_line = raw_file.readline()[:-2] #replace \r\n symbols
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
            in_data = buf
            return in_data
        else:
            print 'You have input wrong data!'
            return []
    except:
        print 'You have input wrong data again!'
        return []

def wrap4files(file_dict, user_fun):
    """
    Function extract line from file from file group and pass it to particular
    function for father mapping.

    Keyword arguments:
    file_dict -- dictionary which contains names of working files'
    user_fun -- user function
    """
    for files in enumerate(sorted(file_dict)):# Open binary files for reading
        file_num = files[0]
        raw_file = open(file_dict[files[1]],'r')
        for lines in enumerate(raw_file):
            line_num, line = lines[0], lines[1]
            user_fun(file_num,line_num,line)
        raw_file.close()

class Data2File():
    """
    Function takes user_file's object for:
    setting its mode depending on file_num and line_num values;
    composing name of the out file depending on chosen data source groups;
    formatting and writing data to file.

    Keyword arguments:

    """
    def __init__(self,user_file,user_data,file_num,line_num,line):
        self.user_file = user_file
        self.user_data = user_data
        self.file_num = file_num
        self.line_num = line_num
        self.line = line

    def SetFileMode(self,user_file,file_num,line_num):
        """
        Function takes user_file's object for setting its mode depending on
        file_num and line_num values.
        """


if __name__ == "__main__":
#    print get_first_line(file_dict)
#    print [i['bin'] for i in get_available_data(file_dict)[:]]
#    print len([i['bin'] for i in get_available_data(file_dict)[:]])
    p = re.compile('d.*')
#    print p.match('dPhi')
