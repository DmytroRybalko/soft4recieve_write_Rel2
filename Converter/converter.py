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

print get_path(conv_data)['in1']
print
print first_line