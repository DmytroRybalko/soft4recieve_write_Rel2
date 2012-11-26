# -*- coding: utf-8 -*-

"""
This script parse KNS data files which are created by parser_kns.py script.
"""

import glob
import time
from create_file_names import datatime2file_name
from data_structure import full_data
from data_structure import kns1_range, kns2_range, kns3_range
from lib4conv import *
#from wireshark_parser.shark_parser import extract_bin_data

#===============================================================================
# Set path for working files

win_path = {'in1':'c:\\Python26\\Scripts\\Files_Converter\\TEST\\BIN_files\\',
            'in2':'d:\\Test\\KNS\\Parsed_files\\',
            'out':'d:\\Test\\KNS\\Result\\'}
lin_path = {'in1':'/home/dmytro/Python_projects/Files_Converter/BIN_files/',
            'in2':'/home/dmytro/Python_projects/Files_Converter/KNS_parsed_files/',
            'out':'/home/dmytro/Python_projects/Files_Converter/CONVERTED_files/'}
test_path = create_path(win_path,lin_path)
#print test_path['in2']

#===============================================================================
# The script reads three type of files which differ by their contents.
# Files raw_kns_1.dat, raw_kns_2.dat and raw_kns_3.dat are created by parser_kns.py
# script and contain data from KNS1, KNS2 and KNS4 according.
# Script handles files separately. It defines file's type, extract data from it
# and writes into text file.

#===============================================================================
# Call function for transforming .pcap file into .dat file
# Path for .pcap files
cap_file = 'wireshark_03.pcap'
# Choose group's name
group_2 = '24475250020044'
group_4 = '2447525004003c'
group_1 = '24475250010084'
g_name = group_1
# Parse .pcap file into dat file.
#extract_bin_data(test_path['in2'] + cap_file,g_name, test_path['in2'] + 'file_out.dat')

# Set file's name for reading data
file_list = glob.glob(test_path['in2'] + '*.dat')
file_name = file_list[0]
raw_file = open(file_name,'r')

#Define type of file by its first line's size
f_line = raw_file.readline()[:-1]
raw_file.seek(0)
kns_range = {'kns1':kns1_range,'kns2':kns2_range,'kns3':kns3_range}
group_name = ''
print u'Доступные группы данных для восстановления:'
for group in kns_range:
    if len(f_line) == kns_groups_len(full_data,kns_range[group]):
        group_name = group
        print group_name
        for packet in kns_range[group_name]:
            print '\t',full_data['name'][packet],'\t',packet

user_input = eval(raw_input('Введите номера параметров для записи в файл: '))
# Set current kns group

group_range = kns_range[group_name]
#group_range = user_input
print group_range

# Open file for writing head string
in_file_name = group_name
conv_file = open(test_path['out'] + datatime2file_name('etalon_' + in_file_name,''),'w')
kns2file(conv_file,full_data,user_input)
conv_file.close()
# Open file for adding data
#conv_file = open(test_path['out'] + 'data_from_' + in_file_name + '.dat','a')
conv_file = open(test_path['out'] + datatime2file_name('etalon_' + in_file_name,''),'a')

# ====== Main loop =============================================================
start_run = time.clock()
for line in raw_file:
    line = line[:-1] # Delete last 'LR' symbol
    for pos in user_input:
        a0 = full_data['shift'][group_range[0]]
        shift = full_data['shift'][pos] - a0
        size = full_data['size'][pos]
        bom = full_data['BOM'][pos]
        typ = full_data['type'][pos]
        full_data['bin'][pos] = line[shift*2:shift*2 + size/4]# read row from file
        binn = full_data['bin'][pos]
        full_data['val'][pos] = struct.unpack(bom + typ,binn.decode('hex'))[0]
    kns2file(conv_file,full_data,user_input)
conv_file.close()
print 'File has been converted!'
end_run = time.clock()
print 'Executing time:', end_run - start_run, 'sec'