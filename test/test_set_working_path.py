# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
import glob
from soft4recieve_write_Rel2.set_working_path import base_file, fun_path, test_path, in_path
from soft4recieve_write_Rel2.Converter.converter import get_available_data
from soft4recieve_write_Rel2.Converter.converter import sort_file_dict, date_from_bin_file

def test1():
    print 'base_file: \n', base_file, '\n'
    print 'test_files \n', test_path.keys(), '\n'
    print 'fun_path: \n', fun_path, '\n'

def test_main_fun_path():
    """
    Function tests file's path which created by main_fun function.
    """
    from soft4recieve_write_Rel2.main_lib import user_group_name2str

    # Get dictionary of binary files
    sfd = sort_file_dict(test_path['common'])
    # Get full first file's name
    fff_name = sfd[sorted(sfd)[0]]
    print "First file's name: \n", fff_name
    print
    print "Date and time: ", date_from_bin_file(fff_name)
    # Get list of available data
    new_packets = get_available_data(sfd)
    # Get group's names of available data
    group_data = user_group_name2str(new_packets)
    print 'Group\'s names of available data: \n', group_data
    local_path = fun_path['main_fun']
    path = local_path(group_data,date_from_bin_file(fff_name))

    print 'main_fun path file: \n', path, '\n'

if __name__ == "__main__":
    test1()
    test_main_fun_path()
