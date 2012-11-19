# -*- coding: utf-8 -*-

"""
This script converts data from files which have been created by moSINS software or
test4converter.py script into text file. Indeed script provides to user choice
which data he or she can convert. Converted data save into text file.
"""

import glob
import itertools
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
    return tuple(buf)

if __name__ == "__main__":
#    print get_first_line(file_dict)
    print [i['bin'] for i in get_available_data(file_dict)[:]]
    print len([i['bin'] for i in get_available_data(file_dict)[:]])
#    print len(''.join(get_available_data(file_dict)[1]['bin'].split('23')))
