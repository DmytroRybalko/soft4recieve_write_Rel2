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

def change_path(path):
    """
    Function insert slash (/) or backslash (\) in path depending on current OS.
    """
    if sys.platform.startswith('win32') and path.split('/') > 1:
        return path.replace('/','\\')
    elif sys.platform.startswith('linux2') and path.split('\\') > 1:
        return path.replace('\\','/')

cp = change_path
# ============= Set root path to files =========================================

win_root_path = 'd:\\Programming\\Python_Projects\\soft4recieve_write_Rel2\\'
lin_root_path = '/home/dmytro/Knowledge/Programming/Python_Projects/soft4recieve_write_Rel2/'
root_path = {'win32':win_root_path,
             'linux2':lin_root_path}

# Set path to base_data.csv file.
base_file = create_path(root_path) + 'base_data.csv'

#===============================================================================

# =================== Set path for incoming bin-files ==========================

in_path = create_path(root_path) + cp('Converter\\BIN_files\\')

#========= Set Local pathes to files that are created by functions  ============
com_path = create_path(root_path) + cp('Converter\\Converter\\')
# ====== main fucntion=========
# Local path to file which is created by 'main' function
main_path = lambda x, y:'file_has_%s_at%s'%(x,y)
# main_path template description:
# x - string contains group's names of data has been chosed by user.
# x sting extracted from get_user_data function list.
# y - date that is created from the first bin file's name.
# y string is got by function get1st_file_date

# ======== Check data functions ================

# Local path to files which are created by kkp_check_data, sns_check_data and
# kns_check_data functions accordingly
kkp_check_path = lambda f_data:'check_kkp_data_in_bin_%s'%(f_data)
sns_check_path = lambda f_data:'check_sns_data_in_bin_%s'%(f_data)
kns_check_path = lambda f_data:'check_kns_data_in_bin_%s'%(f_data)
# path template description:
# x - date that is created from the first bin file's name.


# ===============================================================
# This structure contains names of services functions which
# mapping data of binary files and paths of files which these functions
# create.

func_pool = {'main_fun':{'func':'extract_data', 'path': main_path},
             'IMU':{'func':'kkp_check_data', 'path': kkp_check_path},
             'SNS':{'func': 'sns_check_data', 'path': sns_check_path},
             'KNS':{'func': 'kns_check_data', 'path': kns_check_path}}

#====================== Set path for testing functions =========================

root_test = create_path(root_path) + cp('Converter\\test\\Converter\\')
test_path = {'get_first_line_r':root_test + cp('get_first_line\\right_test\\'),
             'get_first_line_w':root_test + cp('get_first_line\\wrong_test\\'),
             'common':root_test + cp('test_BIN_files\\'),
             'main_fun':root_test + cp('main_fun\\test_files\\')}

#===============================================================================

# Set format style for output text files
data_style = {'f_style':'.8f','i_style':'d','l_style':'l','s_style':'s'}