# -*- coding: utf-8 -*-

"""
This file contains paths for working files.
"""

# Set root path to all working files.
win_root_path = 'd:\\Programming\\Python_Projects\\soft4recieve_write_Rel2\\'
lin_root_path = '/home/dmytro/Knowledge/Programming/Python_Projects/soft4recieve_write_Rel2/'

# Set path to base_data.csv file.
base_data_path = {'win32':{'in1':win_root_path},
                  'linux2':{'in1':lin_root_path}}
# Get base_data.csv file object
base_file = 'base_data.csv'

# Set path to converter.py

conv_data = {'win32':{'in1':win_root_path +'Converter\\Converter\\BIN_files\\',
                      'out_main':win_root_path + 'Converter\\Converter\\CONVERTED_files\\'},
             'linux2':{'in1':lin_root_path +'/Converter/BIN_files/',
                       'out1':lin_root_path +'/Converter/CONVERTED_files'}}

# Set path for testing functions
test_data = {'win32':{'get_first_line':win_root_path +
                      'Converter\\test\\Converter\\get_first_line\\right_test\\',
                      'common':win_root_path + 'Converter\\Converter\\BIN_files\\'}}

# Set format style for output text files
data_style = {'f_style':'.8f','i_style':'d','l_style':'l','s_style':'s'}