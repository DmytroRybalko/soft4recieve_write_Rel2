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

def test4(**args):
    return "Give me arg1 %s" % args['arg1']

def test2(x,y):
    return "Give me arg1 %s, agr2 %s" % (str(x),str(y))

def test5(**args):
    return "Give me arg1 %s, agr2 %s" % (args['arg1'],args['arg2'])

def test3(x,y,z):
    return "Give me arg1 %s, arg2 %s, arg3 %s" % (str(x),str(y),str(z))

def test6(**args):
    return "Give me arg1 %s, arg2 %s, arg3 %s" % (args['arg1'],args['arg2'],args['arg3'])

def test4(**kargs):
    print "Give me arg1 %s, arg2 %s, arg3 %s" % (kargs['arg1'],kargs['arg2'],kargs['arg3'])

def fabric_fun(fun,**kvargs):
    return 'Result of %s '%fun.__name__, fun(kvargs)

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

def main3(func_pool,args):
    """

    """
    for fun in func_pool:
        print 'I am %s'%fun.__name__
        print fun(**args),'\n'

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

    # Create dict of named arguments
    func_pool2 = (test4,test5,test6)
    kargs = {'arg1':'1','arg2':'2','arg3':'3'}
    print test4(**kargs)
    for fun in func_pool2:
        print 'I am %s'%fun.__name__
        print fun(**kargs),'\n'
#    main3(func_pool,kargs)


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


