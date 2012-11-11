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
print BOM_list