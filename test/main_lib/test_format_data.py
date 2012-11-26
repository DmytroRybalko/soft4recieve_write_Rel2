# -*- coding: utf-8 -*-

"""
This file contains unittests for converter.py.
"""
import unittest
from main_lib import format_data

def test1(data):
    for i in data:
        print format_data(i)

if __name__ == "__main__":
    l1 = [23, 45.678, 'egeq']
    l2 = ['d','.4f','s']
    buf = []
    for a,b in zip(l1, l2):
        buf.append(a.__format__(b) + '\t')
#    print ''.join(buf)[:-1]
    print 'From format_data: '
    test1(l1)
