# -*- coding: utf-8 -*-

"""
This file tests path_valid function.
"""
from soft4recieve_write_Rel2.main_lib import get_path, create_path
from soft4recieve_write_Rel2.set_working_path import root_path, base_file

def test1():
    dic_path = {'win32':{'in':'in path for win','out':'out path for win'},
                    'linux2':{'in':'in path1 for lin','out1':'/home/dmytro/',
                              'out2':'/home/dmytroKnowledge/Programming/Python_Projects/soft4recieve_write_Rel2/'},
                    'mac':{'in':'in path for mac','out':'out path for mac'}}
    dic_path2 = {'win32':'none','linux2':'/home/dmytro'}
    print get_path(dic_path)

def test2():
    print create_path(root_path)
if __name__ == "__main__":
    test1()
    test2()



