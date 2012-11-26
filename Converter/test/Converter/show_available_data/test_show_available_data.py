# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
from Converter.converter import file_dict, get_available_data, show_available_data

if __name__ == "__main__":
    new_packets = get_available_data(file_dict)
    result = show_available_data(new_packets)
    print result