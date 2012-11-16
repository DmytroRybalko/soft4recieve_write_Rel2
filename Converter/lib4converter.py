# -*- coding: utf-8 -*-

"""
This script contains a set of auxiliary functions for converter.py and
test4converter.py scripts.
"""

import glob
from set_working_path import conv_data
from main_lib import *

def wrap4read_files():
    """

    """
    # Create list of files for converting
    file_list = glob.glob(get_path(conv_data)['in1'] + '*.dat')
    # Create dictionary of binary files for converting
    file_dict = sort_files(file_list,'bin')
    row_count = 0
    # Choose first file from file_dict
    for ord_num in sorted(file_dict):
        for ord_num in sorted(file_dict):# Open binary files for reading
            raw_file = open(file_dict[ord_num],'r')
            for line in raw_file:
                row_count += 1
                pass
                # Some function
            raw_file.close()
            pass
        pass


#==============================================================================
# Read first line from first binary file to analyse it
first_line = first_file.read(1100)# My propositions: set this number as constant
first_file.close()

#==============================================================================
# Choose first file from file_dict
first_count = 0
for ord_num in sorted(file_dict):
    if first_count == 0:
        first_file = open(file_dict[ord_num],'r')
    else:
        break
#==============================================================================
# Read first line from first binary file to analyse it
first_line = first_file.read(1100)# My propositions: set this number as constant
first_file.close()
print first_line
