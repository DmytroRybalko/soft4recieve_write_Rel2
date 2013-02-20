# -*- coding: utf-8 -*-

"""
This file contains unittests for get_available_data function in converter.py
"""
import unittest
from soft4recieve_write_Rel2.set_working_path import test_path
from soft4recieve_write_Rel2.Converter.converter import get_available_data, sort_file_dict, get_first_line
from soft4recieve_write_Rel2.data_structure import packets

def test1(file_dict):
    """

    """
    line = get_first_line(file_dict)
    buf, new_pack, buf1 = [], [], []
    group_buf = packets[0]['group']
#    group_buf = ''
    for p in packets:
        p['bin'] = line[p['shift']*2:p['shift']*2 + p['size']*2]
        buf.append(p) # accumulate data for one group
        if group_buf != p['group']: # detecting groups changing
            group_buf = p['group']
            buf1.append(buf.pop(-1))# last packet in buf is belonged to next group. moves it to buf1
            sub_line = ''.join([i['bin'] for i in buf])
            if len(''.join(sub_line.split('23'))):
                new_pack += [p for p in buf if p['cut_name']]
                buf = buf1
            else:
                buf = buf1
            buf1 = []
    return new_pack + buf


if __name__ == "__main__":
    # Create dictionary of binary files for converting
    file_dict = sort_file_dict(test_path['common'])
#    result = test1(file_dict)
#    for i in result:
#        print i['cut_name']
#    print len(result)
    result = get_available_data(file_dict)
    print '==============================='
    print 'Available data: ',set([i['group'] for i in result if i.has_key('group')])
    for i in result:
        print i['cut_name']
#    print packets[0]['group']