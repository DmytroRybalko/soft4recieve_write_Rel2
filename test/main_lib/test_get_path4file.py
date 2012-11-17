# -*- coding: utf-8 -*-

"""
This file tests get_my_path function.
"""
from main_lib import get_path4file


if __name__ == "__main__":
    dic_path = {'win32':{'in':'in path for win','out':'out path for win'},
                'linux2':{'in':'in path1 for lin','out1':'/home/dmytro/',
                          'out2':'/home/dmytroKnowledge/Programming/Python_Projects/soft4recieve_write_Rel2/'},
                'mac':{'in':'in path for mac','out':'out path for mac'}}
#    dic_path2 = {'win32':'none','linux2':'/home/dmytro'}
#    print get_path4file(dic_path,out1,'sfsf.dat')
