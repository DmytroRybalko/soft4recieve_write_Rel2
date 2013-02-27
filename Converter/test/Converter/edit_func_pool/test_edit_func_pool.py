# -*- coding: utf-8 -*-

"""
This file contains unittests for get_available_data function in converter.py
"""
import unittest
import copy
from soft4recieve_write_Rel2.set_working_path import test_path
from soft4recieve_write_Rel2.Converter.mapping_functions import func_pool
from soft4recieve_write_Rel2.Converter.converter import get_available_data, sort_file_dict
from soft4recieve_write_Rel2.Converter.converter import edit_func_pool, get_user_data, show_available_data

def test1(file_dict):
    """

    """
    pass


if __name__ == "__main__":
    # Create dictionary of binary files for converting
    file_dict = sort_file_dict(test_path['common'])
    data = get_available_data(file_dict)
    show_available_data(data)
    user_data = get_user_data(data)
    print '==============================='
    result = edit_func_pool(user_data)
#    print result
    for key in result:
        print result[key]
    print result.keys()
