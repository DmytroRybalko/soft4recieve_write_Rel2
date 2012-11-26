# -*- coding: utf-8 -*-

"""
This is set of functions for mapping and analyse raw SNS data which are recieved
via BINR protocol. Data are stored in text file in hexadecimal representation.
These data are used for validation "moSINS" software data.
"""

import struct
import time
from math import pi, floor, log

# Constants for creating/extraction SNS time
ms_in_day = 86400000 #quantity of milisecond in day
ms_in_hour = 3600000 #quantity of milisecond in hour
ms_in_min = 60000    #quantity of milisecond in minute
ms_in_sec = 1000     #quantity of milisecond in second


def extract_sns_time(string):
    """
    Function extracts SNS time from long double data type and returns it in two
    representations - as string in hh-mm-ss format or as a integer number of
    seconds.

    Keyword arguments:
    string -- hexadecimal string that contains SNS time.
    """
    str2L = list(string)
    buf = []
    # Represent each string symbol as a hex number
    hex_buf = ['0x%s'%(i) for i in str2L]
    # Transform hex data to bin
    bin_buf = [bin(int(i,16)) for i in hex_buf]
    for b in bin_buf:
        b1 = b.lstrip('0b')# replace '0b' from string
        # complete bin number of absented forward zeros
        b2 = ''
        for i in range(4 - len(b1)):
            b2 += '0'
        b1 = b2 + b1
        buf.append(b1)
    b3 = ''.join(buf)
    str2L2 = list(b3)
    Sign = '0b' + str2L2.pop(0) # Extract sign
    Exp = [str2L2.pop(0) for i in range(15)]
    Exp = '0b' + ''.join(Exp) # Extract exponenta
    i = '0b' + str2L2.pop(0)
    Man = '0b' + ''.join(str2L2) # Extract mantissa
    S, E, i, M = int(Sign,2), int(Exp,2), int(i,2), int(Man,2)
#    floatt = (-1)**S*2**(E - 127)*(1 + float(M)/(2**23))
    try:
        floatt = (-1)**S*2**(E - 16383)*(1 + float(M)/(2**63))
    except :
        floatt = 0
   # Define day's number from the week's beginnig
    day = int(floatt/ms_in_day)
    # Define current time of day
    time_of_day = floatt - (ms_in_day*day)
    hour = int(time_of_day/ms_in_hour)
    minute = int((time_of_day - ms_in_hour*hour)/ms_in_min)
    second = int((time_of_day - ms_in_hour*hour - ms_in_min*minute)/ms_in_sec)
    msec = int((time_of_day - ms_in_hour*hour - ms_in_min*minute - ms_in_sec*second))
#    times = second + minute*60 + hour*3600
    times = msec + second*1000 + minute*60000 + hour*3600000
#    print msec, time_of_day - ms_in_hour*hour - ms_in_min*minute - ms_in_sec*second
    return '%2dh-%2dm-%2ds'%(hour,minute,second),(int(floatt/1000))
