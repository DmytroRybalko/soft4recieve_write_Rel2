# -*- coding: utf-8 -*-

"""
This file contains paths for working files.
"""
import sys

def create_path(os_dict):
    """
    Function return dictionary with path for working files depending on current
    OS.

    Keyword arguments:
    os_dict -- dictionary that contains working paths for different OS.
    """
    for os_key in os_dict:
        if sys.platform.startswith(os_key):
            return os_dict[os_key]

# ============= Set root path to files =========================================

win_root_path = 'd:\\Programming\\Python_Projects\\soft4recieve_write_Rel2\\'
lin_root_path = '/home/dmytro/Knowledge/Programming/Python_Projects/soft4recieve_write_Rel2/'
root_path = {'win32':win_root_path,
             'linux2':lin_root_path}

# Set path to base_data.csv file.
base_file = create_path(root_path) + 'base_data.csv'

#===============================================================================

# =================== Set path for incoming bin-files ==========================

in_path = create_path(root_path) + 'Converter\\Converter\\BIN_files\\'

#========= Set Local pathes to files that are created by functions  ============
com_path = create_path(root_path) + 'Converter\\Converter\\'
# ====== main fucntion=========
# Local path to file which is created by 'main' function
main_path = lambda x, y:'file_has_%s_at%s'%(x,y)
# main_path template description:
# x - string contains group's names of data has been chosed by user.
# x sting extracted from get_user_data function list.
# y - data is created from the first bin file's name.
# y string is got by function get1st_file_date

# ============== Local pathes to files that are created by functions  ==========

fun_path = {'main_fun':main_path}

#====================== Set path for testing functions =========================

root_test = create_path(root_path) + 'Converter\\test\\Converter\\'
test_path = {'get_first_line_r':root_test + 'get_first_line\\right_test\\',
             'get_first_line_w':root_test + 'get_first_line\\wrong_test\\',
             'common':root_test + 'test_BIN_files\\',
             'main_fun':root_test + 'main_fun\\test_files\\'}

#===============================================================================

# Set format style for output text files
data_style = {'f_style':'.8f','i_style':'d','l_style':'l','s_style':'s'}