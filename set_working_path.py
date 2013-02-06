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
#==================== Path for functions============================
# Local path to file which is created by 'main' function
main_path = win_root_path + 'Converter\\Converter\\'
# Template lambda x, y:main_path + 'file_has_%sat%s'%(x,y) description:
# x - string contains group's names of data has been chosed by user.
# X sting extracted from get_user_data function list.
# y - data is created from the first bin file's name.
# Y string is got by function get1st_file_date

#===================================================================
conv_data = {'win32':{'in1':win_root_path +'Converter\\Converter\\BIN_files\\',
                      'main_fun': lambda x, y:main_path + 'file_has_%s_at%s'%(x,y)},
             'linux2':{'in1':lin_root_path +'/Converter/BIN_files/',
                       'out1':lin_root_path +'/Converter/CONVERTED_files'}}

#===================================================================

# Set path for testing functions
test_data = {'win32':{'get_first_line':win_root_path +
                      'Converter\\test\\Converter\\get_first_line\\right_test\\',
                      'common':win_root_path + 'Converter\\Converter\\BIN_files\\'}}

# Set format style for output text files
data_style = {'f_style':'.8f','i_style':'d','l_style':'l','s_style':'s'}