# -*- coding: utf-8 -*-

"""
This file contains unittests for get_available_data function in converter.py
"""
import unittest
import glob
from soft4recieve_write_Rel2.main_lib import get_path,sort_files
from soft4recieve_write_Rel2.set_working_path import test_data
from soft4recieve_write_Rel2.Converter.converter import get_available_data

if __name__ == "__main__":
    # Create list of files for converting
    path = ('d:\\Programming\\Python_Projects\\soft4recieve_write_Rel2\\' +
                  'Converter\\Converter\\BIN_files\\')
    # Create dictionary of binary files for converting
    file_list = glob.glob(get_path(test_data)['common'] + '*.dat')
#    file_list = glob.glob(path + '*.dat')
    file_dict = sort_files(file_list,'bin')
#    print file_list
    result = get_available_data(file_dict)
    print 'Available data: ', result