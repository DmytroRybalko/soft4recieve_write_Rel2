# -*- coding: utf-8 -*-

"""
This file contains a set of auxiliary functions which can be used in all
project's files.
"""
import sys
import os.path
import copy

def create_path(os_dict):
    """
    Function return dictionary with path for working files depending on current
    OS.

    Keyword arguments:
    os_dict -- dictionary that contains working paths for different OS.
    """
    for os_key in os_dict:
        if sys.platform.startswith(os_key):
            return os_dict[os_key]

def get_path(os_dict):
    """
    Function validates working path for current OS and returns out_dict
    dictionary for correct path.

    Keyword arguments:
    os_dict -- dictionary that contains working paths for different OS.
    """
    dir_path = create_path(os_dict)
    out_dict = copy.deepcopy(dir_path)
    for p in dir_path:
        if not os.path.exists(dir_path[p]):
            out_dict[p] = 'Your *%s* path is invalid!' % p
    return  out_dict

def get_path4file(os_dict,p_key,file_name,file_mode):
    """
    Function return file object which has path 'p_key' from path_dict, name
    'file_name' and file mode like 'file_mode'.
    """
    try:
        work_path = get_path(os_dict)
        return open(work_path[p_key] + file_name, file_mode)
    except:
        print 'Something wrong this your path!'
