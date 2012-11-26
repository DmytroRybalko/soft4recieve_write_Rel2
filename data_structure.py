# -*- coding: utf-8 -*-

"""
The script is purposed for data structure composition from base csv-file.
"""
import csv
from set_working_path import base_data_path, base_file
from main_lib import get_path4file

# Import data from core csv file for creating file structure
base_data = get_path4file(base_data_path,'in1',base_file,'rb')
bd_csv = csv.reader(base_data,delimiter=';')

size_list, shift_list, bin_list = [],[],[]
type_list, long_name, cut_name, = [],[],[]
val_list, group_list, BOM_list = [],[],[]

for column in bd_csv:
    size_list.append(int(column[0]))
    shift_list.append(int(column[1]))
    type_list.append(column[2])
    long_name.append(column[3])
    cut_name.append(column[4])
    val_list.append(int(column[5]))
    group_list.append(column[6])
    BOM_list.append(column[7])
    bin_list.append('')

long_name = [i.decode('cp1251') for i in long_name]

# Replace data type in type_list on python type data
type_dict = dict([('char','B'),('long','l'),('double','d'),('float','f'),
                  ('int','H'),('ushort','H'),('byte','b'),('unsignedint','I'),
                  ('long double','10s')])
type_list = [type_dict[t] for t in type_list]

# Create data store structure
buf_list = []
for pos in range(len(size_list)):
    buf_dic = {}
    buf_dic['size'] = size_list[pos]
    buf_dic['shift'] = shift_list[pos]
    buf_dic['type'] = type_list[pos]
    buf_dic['name'] = long_name[pos]
    buf_dic['cut_name'] = cut_name[pos]
    buf_dic['val'] = val_list[pos]
    buf_dic['group'] = group_list[pos]
    buf_dic['BOM'] = BOM_list[pos]
    buf_dic['bin'] = bin_list[pos]
    buf_list.append(buf_dic)
    del buf_dic
packets = tuple(buf_list)

if __name__ == "__main__":
    print 'size_list: ', size_list
    print '======================='
    print 'shift_list', shift_list
    print '======================='
    print 'type_list', type_list
    print '======================='
    print 'long_name: '
    for i in long_name:
        print i
    print '======================='
    print 'cut_name', cut_name
    print '======================='
    print 'val_list', val_list
    print '======================='
    print 'group_list', group_list
    print '======================='
    print 'BOM_list', BOM_list
    print '======================='
    print 'bin_list', bin_list
    print packets[2]
    print packets[95]['cut_name']
    print
    print [packets.index(pack) for pack in packets if pack['group'] == 'IMU']
    print 'packet94 name is ', packets[21]['name']