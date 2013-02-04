# -*- coding: utf-8 -*-

"""
This script contains a set of auxiliary functions for mapping KKP data.
"""

def extract_kkp_frame_cell(fr_cel):
    """
    Function extract frame's snd cell's values.

    Keyword arguments:
    fr_cel -- hex string
    """

    if fr_cel > 0 & fr_cel < 205:
        cell = fr_cel%8
        frame = fr_cel/8
    elif fr_cel == 0:
        cell = 0
        frame = 0
    else:
        frame = 1
    return (frame, cell)

def improve_check_kkp_data(fd,file_name,pos_sec=122,pos_count=121):
    """
    Function check validity of the KKP data and displays which data are missed
    or doubled.

    Keyword arguments:
    fd -- full_data structure
    file_name -- current file object for reading
    pos_sec, pos_count -- packet's position number in binary file (kkp second
    and count by default)
    """
    row_count = 0
    buff = []
    for line in file_name:
        row_count += 1
        # Extract kkp second and count.
        kkp_sec = hex_line2val(122,fd,line)[0]
        kkp_count = hex_line2val(121,fd,line)[0]
        # Initialize start ref_sec and ref_count values.
        if row_count == 1:
            ref_sec = kkp_sec
            ref_count = kkp_count
        else:# Accumulation ref_count and ref_sec values.
            if ref_count%200 != 0:
                ref_count += 1
            else:
                ref_count = 1
                ref_sec += 1
        # Dedicate kkp data dublication
        while ref_count > kkp_count:
            ref_count -= 1
            buff.append('%17s\t%d\t%d\n\n' % ('Dublication data, sec, count:',ref_sec,ref_count))
        # Dedicate kkp data missing
        while ref_count < kkp_count:
            buff.append('%17s\t%d\t%d\n\n' % ('Missing data, sec, count:',ref_sec,ref_count))
            ref_count += 1
    return buff