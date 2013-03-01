# -*- coding: utf-8 -*-
"""
This
"""
from soft4recieve_write_Rel2.set_working_path import com_path
import copy

def extract_data(**args):
    """

    """
    return args['group_name']

def check_kkp_data(**args):
    """

    """
    return args['group_name']

def check_sns_data(**args):
    """

    """
    return args['group_name']

def check_kns_data(**args):
    """

    """
    return args['group_name']

# Set dictionary of arguments for mapping functions
glob_args = {'row':None,'file':None,'line':None,'group_name':None,'file_date':None,
             '1st_f_name':None}

# Set structure contains names of services functions which
# mapping data of binary files and paths of files which these functions
# create.

func_pool = {extract_data:{'path': com_path +'file_has_%(group_name)s_at%(file_date)s.dat'},
             check_kkp_data:{'group':'IMU',
                             'quest':'Does check kkp data? (y/n): ',
                             'path':com_path +'kkp_check_from_%(1st_f_name)s.dat'},
             check_sns_data:{'group':'SNS',
                             'quest':'Does check sns data? (y/n): ',
                             'path':com_path +'sns_check_from_%(1st_f_name)s.dat'},
             check_kns_data:{'group':'KNS',
                             'quest':'Does check kns data? (y/n): ',
                             'path':com_path +'kns_check_from_%(1st_f_name)s.dat'}}

if __name__ == "__main__":
    dic = {}
    dic['group_name'] = 'IMU_SINS'
    dic['file_date'] = '02-02-2013_10-14'
    dic['1st_f_name'] = 'binMoSINS_02-02-2013_10-14'
    # Test path from func_pool
    template = func_pool[extract_data]
    path = template['path'] % dic
#    print path
    for func, data in func_pool.items():
        print func.__name__
        print data['path'] % dic
#        print func['path'] % dic

    uc = {1:'Does check kns data? (y/n): ',
          2:'Does check kkp data? (y/n): ',
          3:'Does check sns data? (y/n): '}
#    [uc.pop(key) for key, quest in uc.items() if raw_input(quest) == 'n']
#    print uc
#    nfp = copy.deepcopy(func_pool)
#    for key, val in nfp.items():
#        try:
#            if raw_input(val['quest']) == 'n':
#                nfp.pop(key)
#        except KeyError:
#            pass
#    print nfp.keys()
