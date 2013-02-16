# -*- coding: utf-8 -*-

"""
This file contains unittests for get_available_data function in converter.py
"""
import unittest
from soft4recieve_write_Rel2.set_working_path import test_path
from soft4recieve_write_Rel2.Converter.converter import get_available_data, sort_file_dict

if __name__ == "__main__":
    # Create dictionary of binary files for converting
    file_dict = sort_file_dict(test_path['common'])
    result = get_available_data(file_dict)
    print '==============================='
    print 'Available data: ',set([i['group'] for i in result if i.has_key('group')])