# -*- coding: utf-8 -*-
"""
This
"""
from soft4recieve_write_Rel2.set_working_path import com_path

def extract_data(**args):
    """

    """
    pass

def check_kkp_data(**args):
    """

    """
    pass

def check_sns_data(**args):
    """

    """
    pass

def check_kns_data(**args):
    """

    """
    pass


# Set structure contains names of services functions which
# mapping data of binary files and paths of files which these functions
# create.

func_pool = {'func1':{'func':extract_data,
                      'path': com_path +'file_has_%(group_name)s_at%(file_date)s.dat'},
             'func2':{'func':check_kkp_data, 'group':'IMU',
                      'path':com_path +'kkp_check_from%(file_date)s.dat'},
             'func3':{'func':check_sns_data, 'group':'SNS',
                      'path':com_path +'sns_check_from%(file_date)s.dat'},
             'func4':{'func4':check_kns_data, 'group':'KNS',
                      'path':com_path +'sns_check_from%(file_date)s.dat'}}

if __name__ == "__main__":
    dic = {}
    dic['group_name'] = 'IMU_SINS'
    dic['file_date'] = '02-02-2013_10-14'
    # Test path from func_pool
    template = func_pool['func1']
    path = template['path'] % dic
    print path
