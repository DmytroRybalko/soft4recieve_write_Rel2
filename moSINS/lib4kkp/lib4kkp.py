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