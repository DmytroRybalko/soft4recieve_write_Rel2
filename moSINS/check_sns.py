# -*- coding: utf-8 -*-
"""
Скрипт для тестирования работы ПО MO_SINS.exe в части записи данных с АП СНС
"""
import time
from My_libraries.create_file_names import datatime2file_name
from lib4sns.SNS_test import *
from data_structure import full_data

def extract_packet85():
    # Raw binary file
    bin_fname = 'sns_demo11-05-12.txt'#'TEST1.txt'#
    f_name = open(file_path + bin_fname,'rb')
    # Binary file after editing
    raw_fname = 'sns_demo_edit_' + 'from' + bin_fname.split('.')[0] + '.txt'
    raw_file = open(file_path + raw_fname,'w')
    # Text file after extracting packets
    packet_name = '85'
    txt_fname = 'packet' + packet_name + 'from' + bin_fname.split('.')[0] + '.txt'
    txt_file = open(file_path + txt_fname,'w')
    # Edit binary data file
    read_bin2txt(f_name,raw_file)
    f_name.close()
    # Extract data from editoring binary file to text file
    f_name = open(file_path + raw_fname,'r')
    # Set order and double values data type in packet
    tup85 = (16,16,16,20,8)
    p85 = sep_pack_in_data(f_name,packet_name)
    # Extract data from packet
    for subpack in p85:
        raw_data = sep_data_in_pack(subpack,tup85)
        txt_file.write(extract_data(raw_data))
    txt_file.close()
    print 'File ' + txt_fname + ' has been written!'
    f_name.close()

def extract_packet88():
    # Edit raw text file
    f_name = open(test_path + file_name,'rb')
    f_write = open(test_path + 'edit_' + file_name,'w')
    # edit_qt_test(f_name,f_write)
    edit_qt_test2(f_name,f_write)
    f_name.close()
    f_write.close()
    # Separate binary data into packets
    f_name = open(test_path + 'edit_' + file_name,'rb')
    f_write = open(test_path + 'pack_' + file_name,'w')
    edit_packet88_60(f_name,f_write)
    f_write.close()
    # Extract data from packet to file
    f_name = open(test_path + 'pack_' + file_name,'r')
    write_p88 = open(test_path + 'p88_from' + file_name,'w')
    tup88 = (16,16,16,8,20)
    p88 = sep_pack_in_data(f_name,'88')
    for subpack in p88:
        raw_data = sep_data_in_pack(subpack,tup88)
        write_p88.write(extract_data(raw_data))
    write_p88.close()
    print 'File ' + 'p88_from' + file_name + ' has been written!'
    f_name.close()

def extract_packet60():
    # Extract packet 60 from file
    f_name = open(file_path + 'pack_88_60.txt','r')
    write_p60 = open(file_path + 'packets_60.txt','w')
    tup60 = (2,2,8,8)
    p60 = sep_pack_in_data(f_name,'60')
#    print p60[0]
    # Extract data from packet to file
    for subpack in p60:
        raw_data = sep_data_in_pack(subpack,tup60)
    #    print sep_data_in_pack(p60[0],tup60)
        nGPS = struct.unpack('<B',raw_data[0].decode('hex'))[0]
        nGLO = struct.unpack('<B',raw_data[1].decode('hex'))[0]
        HDOP = struct.unpack('<f',raw_data[2].decode('hex'))[0]
        VDOP = struct.unpack('<f',raw_data[3].decode('hex'))[0]
        out = '%5d %5d %19.6f %19.6f\n'%(nGPS, nGLO, HDOP, VDOP)
        write_p60.write(out)
    write_p60.close()
    print 'File ' + 'packets_60.txt' + ' has been written!'
    f_name.close()

def extract_packets_88_60():
    # Edit raw text file
    f_name = open(base_path + file_name,'r')
    f_write = open(res_path + 'edit_' + file_name,'w')
    edit_qt_test(f_name,f_write)
    f_name.close()
    f_write.close()
    # Separate binary data into packets
    f_name = open(res_path + 'edit_' + file_name,'rb')
#    f_name = open(res_path + 'pack_test_88_60_15_06_2012.txt','rb')
    f_write = open(res_path + 'pack_' + file_name,'w')
    packets_name = ('88','60')
#    packets_name = ('88')
    extract_packets(f_name,f_write,packets_name)
    f_name.close()
    f_write.close()
    # Extract data from packets to file
    f_name = open(res_path + 'pack_' + file_name,'r')
#    f_write = open(res_path + datatime2file_name('extracted_from_' + file_name,'','txt'),'w')
    f_write = open(res_path + 'extracted_from_' + file_name,'w')
    f_write88 = open(res_path + 'sns_etalon' + file_name,'w')
    tup88 = (16,16,16,8,20)
    tup60 = (2,2,8,8)
    # Move packets to list
    buff_88_60, buff_88 = [],[]
    for packet in f_name:
        buff_88_60.append(packet)
        if packet[0:2] == '88':
            buff_88.append(packet)
    # Write packet 88 to file
    print u'Широта -- 0'
    print u'Долгота -- 1'
    print u'Высота -- 2'
    print u'CKO -- 3'
    print u'Время -- 4'
    user_input = eval(raw_input('Введите номера параметров для записи в файл: '))
    binary = raw_input('Нужно ли выводить бинарные данные? (Y/N): ')
    # out_data = (0,1,2,4)
    out_data = user_input
    packet2file(buff_88,tup88,out_data,f_write88,binary)
    # print buff_88_60[43:45]
    # group = (10,11,12,13,14,6,7,8,9)
    # Mapping each packet
    trig = set([])
    buf2 = []
    count = 0
    for packet in buff_88_60:
        if packet[0:2] == '88':
            count += 1
            if count == 35: print packet
            trig.add('88')
            raw_data_88 = sep_data_in_pack(packet[2:-1],tup88)
            full_data['val'][10:15] = extract_data(raw_data_88)
        if packet[0:2] == '60':
            trig.add('60')
            raw_data_60 = sep_data_in_pack(packet[2:-1],tup60)
            nGPS = struct.unpack('<B',raw_data_60[0].decode('hex'))[0]
            nGLO = struct.unpack('<B',raw_data_60[1].decode('hex'))[0]
            HDOP = struct.unpack('<f',raw_data_60[2].decode('hex'))[0]
            VDOP = struct.unpack('<f',raw_data_60[3].decode('hex'))[0]
#            out = '%19d %19d %19.6f %19.6f\n'%(nGPS, nGLO, HDOP, VDOP)
            full_data['val'][6:10] = (nGPS, nGLO, HDOP, VDOP)
        if len(trig) < 2:# If other packet didn't came mapping current packet
            buf1 = []
            for pos in (10,11,12,13,14,6,7,8,9):
                pack = full_data['val'][pos]
                if isinstance(pack,float):
                    buf1.append(pack.__format__('^19.8f') + '\t')
                elif isinstance(pack,int):
                    buf1.append(pack.__format__('4d') + '\t')
                else:
                    buf1.append(pack.__format__('12s') + '\t')
            buf1.append('\n')
            buf2.append(buf1)
        else: # If 
            for pos,i in zip((6,7,8,9),(0,1,2,3)):  # Adding new elements
                pack = full_data['val'][pos]
                if isinstance(pack,float):
                    buf2[-1][5+i] = pack.__format__('^19.8f') + '\t'
                elif isinstance(pack,int):
                    buf2[-1][5+i] = pack.__format__('4d') + '\t'
                else:
                    buf2[-1][5+i] = pack.__format__('12s') + '\t'
            for sub in buf2:
                f_write.write(''.join(sub))
            trig.clear()
            buf2 = []
    f_write.close()
    print 'File ' + 'extracted_pack_88_60.txt' + ' has been written!'
    f_name.close()

if __name__ == '__main__':
    # Set file's paths
    base_path = 'd:\\Test\\SNS\\Base\\'
    test_path = 'd:\\Test\\SNS\\Testing\\'
    res_path = 'd:\\Test\\SNS\\Result\\'
    file_name = 'packets_88_60_18_06_2012-01.txt'
#    file_name = 'packets_88_60_18_06_2012-04.txt'
    start_run = time.clock()
    extract_packets_88_60()
#    extract_packet85()
#    extract_packet88()
#    extract_packet60()
    end_run = time.clock()
    print 'Executing time:', end_run - start_run, 'sec'