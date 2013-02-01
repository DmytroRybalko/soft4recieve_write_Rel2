# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
import glob
from soft4recieve_write_Rel2.main_lib import get_path,sort_files
from soft4recieve_write_Rel2.set_working_path import test_data
from soft4recieve_write_Rel2.Converter.converter import get_available_data
from soft4recieve_write_Rel2.Converter.converter import show_available_data
from soft4recieve_write_Rel2.Converter.converter import get_user_data

if __name__ == "__main__":
    # Create list of files for converting
    file_list = glob.glob(get_path(test_data)['common'] + '*.dat')
    # Create dictionary of binary files for converting
    file_dict = sort_files(file_list,'bin')
    # Get list of available data
    new_packets = get_available_data(file_dict)
    # Show list of available data
    show_available_data(new_packets)
    print 'new_packets: ', len(new_packets)
    result = get_user_data(new_packets)
    print 'len: ', len(result)
    for i in result:
        print i['cut_name']