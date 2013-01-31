# -*- coding: utf-8 -*-

"""
This file contains unittests for get_first_line function
"""

import unittest
import glob
from soft4recieve_write_Rel2.main_lib import get_path,sort_files
from soft4recieve_write_Rel2.set_working_path import test_data
from soft4recieve_write_Rel2.Converter.converter import get_first_line

if __name__ == "__main__":
    right_path = ('d:\\Programming\\Python_Projects\\soft4recieve_write_Rel2\\' +
                  '\\Converter\\test\\Converter\\get_first_line\\right_test\\')
    # Create list of files for converting
#    file_list = glob.glob(get_path(test_data)['get_first_line'] + '*.dat')
    file_list = glob.glob(right_path + '*.dat')
    # Create dictionary of binary files for converting
    file_dict = sort_files(file_list,'bin')
    first_line = get_first_line(file_dict)
    print 'First line: ', first_line
