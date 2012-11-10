# -*- coding: utf-8 -*-

"""
This file contains a set of auxiliary functions which can be used in all
project's files.
"""
import sys
import os.path

def create_path(os_dict):
    """ Function create path for working fies depending on current OS.

    Keyword arguments:
    os_dict -- dictionary that contains working paths for different OS.

    Output:
    dir_path -- string that contains current working directories.
    """

    for os_key in os_dict:
        if sys.platform.startswith(os_key):
            for path in os_dict[os_key]:
                if not os.path.exists(os_dict[os_key][path]):
                    print 'Your %s path isn\'t valid!' % path
                else:
                    print 'Your path:', os_dict[os_key][path]
            break

if __name__ == "__main__":
    dic_path = {'win32':{'in':'in path for win','out':'out path for win'},
                'linux2':{'in':'in path1 for lin','out1':'/home/dmytro',
                          'out2':'out path2 for lin'},
                'mac':{'in':'in path for mac','out':'out path for mac'}}
    dic_path2 = {'win32':'','linux2':'/home/dmytro'}
    create_path(dic_path)