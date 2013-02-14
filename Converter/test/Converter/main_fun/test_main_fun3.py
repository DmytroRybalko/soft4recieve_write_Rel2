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


def main4(sfd,func_pool,arg):
    """
    This function write data produced by servise function in its own file.

    sfd -- dictionary of sorted files for reading
    """
    for arg['arg1'], arg['arg2'], arg['arg3'] in line_from_file(sfd):#read data from files
        for fun in (test4,):
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
                fun.__setattr__('my_file' ,fun.__name__ + '.dat')

def main5(sfd,func_pool,arg):
    """
    This function write data produced by servise functions in theis own files.

    sfd -- dictionary of sorted files for reading
    """
    # Set path for files produced by test functions
    test1 = test_path['main_fun'] + 'test1.dat'
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
                fun.__setattr__('my_file' ,fun.__name__ + '.dat')

if __name__ == "__main__":
    print 'Test main3 func\n=================='
    # Create dict of named arguments
    func_pool2 = (test4,test5,test6)
#    kargs = {'arg1':'1','arg2':'2','arg3':'3'}
    kargs = {'arg1':None,'arg2':None,'arg3':None}
#    main3(func_pool2,kargs)
    print '==================\n'
    print 'Test main4 func\n=================='
    # Get path to test files
    sfd = sort_file_dict(test_path['main_fun'])
    main5(sfd,func_pool2,kargs)
    print '==================\n'

    print "=================================================="
#    print (test3.__code__.co_varnames)
#    print 'Attribute test'
#    test1('3')
#    print  dir(test1)
#    print test1.__dict __
#    help(test1.func_dict)
#    test1.my_file_name = 'test.dat'
#    test1.__setattr__('my_file_name','test\\test.dat')
#    print dir(test1)
#    print test1.my_file_name


