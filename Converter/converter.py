# -*- coding: utf-8 -*-

"""
This script converts data from files which have been created by moSINS software or
test4converter.py script into text file. Indeed script provides to user choice
which data he or she can convert. Converted data save into text file.
"""

import glob
from set_working_path import conv_data
from main_lib import *

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

def get_available_data():
    """
    Define groups of sources (SNS,KNS,IMU,ODO,SINS) which data has been written
    to raw files.

    Keyword arguments:

    """



if __name__ == "__main__":
    # Create list of files for converting
    file_list = glob.glob(get_path(conv_data)['in1'] + '*.dat')
    # Create dictionary of binary files for converting
    file_dict = sort_files(file_list,'bin')
    row_count = 0
    #    print map(sorted,[[2,1],[14,5]])
    #    print wrap4read_files(get_first_line)
    print wrap4read_files()
    we = ['qwe','4','ref','d35gtr']
    #    print map(methodcaller('isalpha'),we)
    s = 'isalpha'