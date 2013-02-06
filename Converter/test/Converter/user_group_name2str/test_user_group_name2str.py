# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
import glob
from soft4recieve_write_Rel2.main_lib import get_path,sort_files
from soft4recieve_write_Rel2.set_working_path import conv_data, test_data
from soft4recieve_write_Rel2.Converter.converter import get_available_data
from soft4recieve_write_Rel2.Converter.converter import show_available_data
from soft4recieve_write_Rel2.Converter.converter import get_user_data
from soft4recieve_write_Rel2.Converter.converter import user_group_name2str

if __name__ == "__main__":
    # Create list of files for converting
    file_list = glob.glob(get_path(test_data)['common'] + '*.dat')
    # Create dictionary of binary files for converting
    file_dict = sort_files(file_list,'bin')
    # Get list of available data
    new_packets = get_available_data(file_dict)
    # Show list of available data
    show_available_data(new_packets)
    user_data = get_user_data(new_packets)
#    print user_data
    result = user_group_name2str(user_data)
    print 'Data group name is: ', result
