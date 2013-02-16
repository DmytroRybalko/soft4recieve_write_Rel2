# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
from soft4recieve_write_Rel2.set_working_path import test_path
from soft4recieve_write_Rel2.Converter.converter import get_available_data
from soft4recieve_write_Rel2.Converter.converter import sort_file_dict
from soft4recieve_write_Rel2.Converter.converter import show_available_data
from soft4recieve_write_Rel2.Converter.converter import get_user_data

if __name__ == "__main__":
    # Create dictionary of binary files for converting
    file_dict = sort_file_dict(test_path['common'])
    # Get list of available data
    new_packets = get_available_data(file_dict)
    # Show list of available data
    show_available_data(new_packets)
    print 'new_packets: ', len(new_packets)
#    print type(new_packets)
#    print new_packets[0:2]
#    name = lambda name:([p for p in new_packets if p['cut_name'] == name])
#    buf = name('Sec') + name('Count')
#    print 'buf = ',buf
    result = get_user_data(new_packets)
    print 'len: ', len(result)
    for i in result:
        print i['cut_name']