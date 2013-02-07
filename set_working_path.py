# -*- coding: utf-8 -*-

"""
This file contains paths for working files.
"""

# ============= Set root path to all working files.
win_root_path = 'd:\\Programming\\Python_Projects\\soft4recieve_write_Rel2\\'
lin_root_path = '/home/dmytro/Knowledge/Programming/Python_Projects/soft4recieve_write_Rel2/'
root_path = {'win32':win_root_path,
             'linux2':lin_root_path}
# Set path to base_data.csv file.
base_file = 'base_data.csv'

#==================== Set paths for functions ============================

# ====== main fucntion=========
# Local path to file which is created by 'main' function
main_path = lambda x, y:'BIN_files\\' + 'file_has_%s_at%s'%(x,y)
# main_path template description:
# x - string contains group's names of data has been chosed by user.
# x sting extracted from get_user_data function list.
# y - data is created from the first bin file's name.
# y string is got by function get1st_file_date

# =================== Common pathes=======
root_main = 'Converter\\Converter\\'
work_path = {'in1': root_main + 'BIN_files\\',
             'main_fun':main_path}

#====================== Set path for testing functions =========================
root_test = 'Converter\\test\\Converter\\'
test_path = {'get_first_line_r':root_test + 'get_first_line\\right_test\\',
             'get_first_line_w':root_test + 'get_first_line\\wrong_test\\',
             'common':root_test + 'BIN_files\\'}

#===============================================================================

# ============== Delete this!!!!!!================
#test_data = {'win32':{'get_first_line':win_root_path +
#                      'Converter\\test\\Converter\\get_first_line\\right_test\\',
#                      'common':win_root_path + 'Converter\\Converter\\BIN_files\\'}}
#=========================================================


# Set format style for output text files
data_style = {'f_style':'.8f','i_style':'d','l_style':'l','s_style':'s'}