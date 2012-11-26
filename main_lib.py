# -*- coding: utf-8 -*-

"""
This file contains a set of auxiliary functions which can be used in all
project's files.
"""
import sys
import os.path
import copy
from set_working_path import data_style

def create_path(os_dict):
    """
    Function return dictionary with path for working files depending on current
    OS.

    Keyword arguments:
    os_dict -- dictionary that contains working paths for different OS.
    """
    for os_key in os_dict:
        if sys.platform.startswith(os_key):
            return os_dict[os_key]

def get_path(os_dict):
    """
    Function validates working path for current OS and returns out_dict
    dictionary for correct path.

    Keyword arguments:
    os_dict -- dictionary that contains working paths for different OS.
    """
    dir_path = create_path(os_dict)
    out_dict = copy.deepcopy(dir_path)
    for p in dir_path:
        if not os.path.exists(dir_path[p]):
            out_dict[p] = 'Your *%s* path is invalid!' % p
    return  out_dict

def get_path4file(os_dict,p_key,file_name,file_mode):
    """
    Function return file object which has path 'p_key' from path_dict, name
    'file_name' and file mode like 'file_mode'.
    """
    try:
        work_path = get_path(os_dict)
        return open(work_path[p_key] + file_name, file_mode)
    except:
        print 'Something wrong this your path!'

def sort_files(file_list,sep=''):
    # функция выполняет сортировку списка имен файлов, содержащих числовые значения
    # file_list - список имен файлов
    # Считываем данные из файла
    key,val = [],[]
    if sep != '':
        FL = []
        for fname in file_list:
            fn4d = fname.split('\\')[-1][:(-4)] #Разбиваем строку по разделителю "\\", выделяем последний элемент списка и удаляем последние 4 символа:'
            if len(fn4d.split(sep)) > 1:        # if 'sep' in file name - add it to list
                FL.append(fname)
    else:
        FL = file_list[:]
    for fname in FL:
        fn4d = fname.split('\\')[-1][:(-4)] #Разбиваем строку по разделителю "\\", выделяем последний элемент списка и удаляем последние 4 символа:'
        buf1 = fn4d.split('-').pop(-1)# choose string that conteins hh_mm
        buf2 = buf1.split('.')        # split string into two numbers
        part1 = int(buf2[0])*100
        part2 = int(buf2[1])
        number = part1 + part2        # form complex number with hours and minutes
        key.append(int(number))
        val.append(fname)
        D = dict(zip(key,val)) # Формируем словарь вида {num:'file name'}
    return D

def format_data(data):
    """
    Function format data depending on data's type.
    """
    if isinstance(data,float):
        return data.__format__(data_style['f_style'])
    elif isinstance(data,int):
        return data.__format__(data_style['i_style'])
    elif isinstance(data,long):
        return data.__format__(data_style['l_style'])
    elif isinstance(data,str):
        return data.__format__(data_style['s_style'])
    else:
        print 'Problem with type!'
        return None
