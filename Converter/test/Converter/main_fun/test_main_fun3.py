# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
import glob
from soft4recieve_write_Rel2.main_lib import user_group_name2str
from soft4recieve_write_Rel2.set_working_path import fun_path, test_path
from soft4recieve_write_Rel2.Converter.converter import (get_available_data,
    main_fun, sort_file_dict, date_from_bin_file, line_from_file)

def test4(**args):
    return "Give me arg1 %s\n" % args['arg1']

def test5(**args):
    return "Give me arg1 %s, agr2 %s\n" % (args['arg1'],args['arg2'])

def test6(**args):
    return "Give me arg1 %s, arg2 %s, arg3 %s" % (args['arg1'],args['arg2'],args['arg3'])


def main4(sfd,func_pool,arg,file_path='.dat'):
    """
    This function write data produced by servise function in its own file.

    TODO: describe all tests as documentation for further displaying.For example
    This func:
    1 ....do something...............
    2 ....do something...............
    ...................

    sfd -- dictionary of sorted files for reading
    """
    for arg['arg1'], arg['arg2'], arg['arg3'] in line_from_file(sfd):#read data from files
        for fun in func_pool:
            try:
                # Create file's object from function's attribute that stores path to writing file
                func_file = open(fun.my_file,'a')
                func_file.write(fun(**arg)+'')
                func_file.close()
            except:
                # Create file, write head string and first line
                f_test1 = open(fun.__name__ + '.dat','w')
                f_test1.write('This is head of %s\n\n'%fun.__name__)
                f_test1.write(fun(**arg)+'')
                f_test1.close()
                # Attach file's name as function attribute
                fun.__setattr__('my_file' ,fun.__name__ + file_path)
    print 'File name is %s'%fun.my_file

if __name__ == "__main__":
    # Get path to test files
    sfd = sort_file_dict(test_path['main_fun'])
    # Create dict of named arguments
    func_pool = (test4,test5,test6)
    kargs = {'arg1':None,'arg2':None,'arg3':None}
    print 'Test main3 func\n=================='
    print 'Main3 function calls one function that creates its file and write data in it.\n'
    main4(sfd,(test6,),kargs)
    print '==================\n'
    print 'Main function calls pool of functions each of which creates its file and write data in it.\n'
    main4(sfd,func_pool,kargs)


