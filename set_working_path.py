# -*- coding: utf-8 -*-

"""
This file contains paths for working files.
"""
from soft4recieve_write_Rel2.main_lib import get_my_path

# Set root path to all working files.
win_root_path = 'd:\\Programming\\Python_Projects\\soft4recieve_write_Rel2\\'
lin_root_path = '/home/dmytro/Knowledge/Programming/Python_Projects/soft4recieve_write_Rel2/'

# Set path to base_data.csv file.
base_data_path = {'win32':{'in1':win_root_path},
                  'linux2':{'in1':lin_root_path}}
# Get base_data.csv file object
base_data = get_my_path(base_data_path,'in1','base_data.csv','rb')
