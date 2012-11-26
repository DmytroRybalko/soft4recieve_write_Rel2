# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
import glob
from Converter.converter import file_dict, wrap4files
from main_lib import sort_files
from data_structure import packets

# Create list of files for converting
file_list = glob.glob('*.dat')
# Create dictionary of binary files for converting
file_dict = sort_files(file_list,'bin')

def user_fun(*args):
    packets, line, num_file, num_line = args[0], args[1], args[2], args[3]
    return 'No.File: %d No.line: %d\nData: %s\n' % (num_file + 1,num_line + 1,line)

def user_fun2(*args):
    print 'user_fun2: ', args[0]

if __name__ == "__main__":
    print file_dict
    test_file = open('test_file.dat','w')
    wrap4files(file_dict,packets,user_fun,test_file)
#    wrap4files(file_dict,user_fun2)