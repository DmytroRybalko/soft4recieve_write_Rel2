# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
from Converter.converter import (file_dict, get_user_data, show_available_data,
                                 get_available_data)

if __name__ == "__main__":
    new_packets = get_available_data(file_dict)
    show_available_data(new_packets)
    print 'new_packets: ', len(new_packets)
    result = get_user_data(new_packets)
    print 'len: ', len(result)
    for i in result:
        print i['cut_name']