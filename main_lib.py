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
            print 'Your path:',
            return os_dict[os_key]




if __name__ == "__main__":
    dic_path = {'win32':{'in':'in path for win','out':'out path for win'},
                'linux2':{'in':'in path1 for lin','out1':'/home/dmytro',
                          'out2':'out path2 for lin'},
                'mac':{'in':'in path for mac','out':'out path for mac'}}
    dic_path2 = {'win32':'none','linux2':'/home/dmytro'}
    print create_path(dic_path)
#    dic_path3 = copy.deepcopy(dic_path)
#    print dic_path3
#    del dic_path3['win32']['in']
#    print dic_path3

#out_dict = copy.deepcopy(os_dict)
#for os_key in os_dict:
#    if sys.platform.startswith(os_key):
#        for path in os_dict[os_key]:
#            if not os.path.exists(os_dict[os_key][path]):
#                print 'Your *%s* path is invalid!' % path
#                del out_dict[os_key][path]
#            #                    return None
#            else:
#                pass
#        print 'Your valid path:',
#        return out_dict[os_key]