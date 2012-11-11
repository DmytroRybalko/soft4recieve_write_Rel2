# -*- coding: utf-8 -*-

"""
The script is purposed for data structure composition from base csv-file.
"""
import csv
from soft4recieve_write_Rel2.set_working_path import base_data

# Import data from core csv file for creating file structure
bd_csv = csv.reader(base_data,delimiter=';')

out_list, size_list, shift_list = [],[],[]
type_list, long_name, cut_name, = [],[],[]
val_list, group_list, BOM_list = [],[],[]

for column in bd_csv:
    out_list.append(int(column[0]))
    size_list.append(int(column[1]))
    shift_list.append(int(column[2]))
    type_list.append(column[3])
    long_name.append(column[4])
    cut_name.append(column[5])
    val_list.append(int(column[6]))
    group_list.append(column[7])
    BOM_list.append(column[8])

# Create data store structure
buf_list = []
for pos in range(len(out_list)):
    buf_dic = {}
    buf_dic['out'] = out_list[pos]
    buf_dic['size'] = size_list[pos]
    buf_dic['shift'] = shift_list[pos]
    buf_dic['type'] = type_list[pos]
    buf_dic['name'] = long_name[pos].decode('cp1251')
    buf_dic['cut_name'] = cut_name[pos]
    buf_dic['val'] = val_list[pos]
    buf_dic['group'] = group_list[pos]
    buf_dic['BOM'] = BOM_list[pos]
    buf_list.append(buf_dic)
    del buf_dic
packets = tuple(buf_list)

if __name__ == "__main__":
#    print BOM_list
    print packets[3]
    print packets[95]['cut_name']
    print
    print [packets.index(pack) for pack in packets if pack['group'] == 'IMU']
    print 'packet94 name is ', packets[21]['name']
#    er = (34,'gerg','4566',45,'eggw')
#    print er.index(45)