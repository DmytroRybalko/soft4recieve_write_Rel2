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

def test1(x):
    return "Give me arg1 %s" % str(x)

def test2(x,y):
    return "Give me arg1 %s, agr2 %s" % (str(x),str(y))

def test3(x,y,z):
    return "Give me arg1 %s, arg2 %s, arg3 %s" % (str(x),str(y),str(z))

def test4(**args):
    return "Give me arg1 %s" % args['arg1']

def test5(**args):
    return "Give me arg1 %s, agr2 %s" % (args['arg1'],args['arg2'])

def test6(**args):
    return "Give me arg1 %s, arg2 %s, arg3 %s" % (args['arg1'],args['arg2'],args['arg3'])

def main1(func_pool,func_args):
    """
    This is first part of main function which demostrade pathing tupels of
    arguments into dictionary of functions.
    """
    for fun, arg in zip(func_pool,func_args):
        print '%s, I am %s'%(fun(*func_args[fun.__name__]), fun.__name__)

def main2():
    """
    This is the second part of main function which separate tupels of arguments
    for functions according fuctions.

    vargs -- list of tuples with arguments
    """
    # Get dictionary of binary files
    sfd = sort_file_dict(test_path['main_fun'])
    for f, r, l in line_from_file(sfd):#read data from files
        func_args = {'test1':(f,),'test2':(f,r),'test3':(f,r,l)}
        for fun, arg in zip(func_pool,func_args):
            print 'I am %s'%fun.__name__
            print fun(*func_args[fun.__name__]),'\n'

def main3(func_pool,arg):
    """
    This function extract data from list of files, number of files and number
    of lines in file and pass theirs as arguments to pool of function.
    """
    # Get dictionary of binary files
    sfd = sort_file_dict(test_path['main_fun'])
    for arg['arg1'], arg['arg2'], arg['arg3'] in line_from_file(sfd):#read data from files
        for fun in func_pool:
            print 'I am %s'%fun.__name__
            print fun(**arg),'\n'

def main4(sfd,func_pool,arg):
    """
    This function write data produced by servise functions in theis own files.

    sfd -- dictionary of sorted files for reading
    """
    # Set path for files produced by test functions
    test1 = test_path['main_fun'] + 'test1.dat'
    for arg['arg1'], arg['arg2'], arg['arg3'] in line_from_file(sfd):#read data from files
        for fun in (test6,):
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

#                print 'I am %s'%fun.__name__
#    print fun.__getattribute__('my_file')
#    print 'Func got attribute', fun.my_file
#    print dir(fun)

if __name__ == "__main__":
    print 'Test main1 func\n=================='
    # Create pool of functions
    func_pool = (test1,test2,test3)
    # Create dict that connects function's name and tuple of arguments
    func_args = {'test1':'a','test2':('b','c'),'test3':('b','a','c')}
#    main1(func_pool,func_args)
    print '==================\n'
    print 'Test main2 func\n=================='
#    main2()
    print '==================\n'
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
    main4(sfd,func_pool2,kargs)
    print '==================\n'

    # Get dictionary of binary files
    sfd = sort_file_dict(test_path['common'])
    # Get full first file's name
    fff_name = sfd[sorted(sfd)[0]]
    # Get list of available data
    new_packets = get_available_data(sfd)
    # Get group's names of available data
    group_data = user_group_name2str(new_packets)
    print 'Group\'s names of available data: \n', group_data
    local_path = fun_path['main_fun']
    path = local_path(group_data,date_from_bin_file(fff_name))



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


