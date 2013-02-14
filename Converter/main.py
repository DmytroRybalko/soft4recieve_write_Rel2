# -*- coding: utf-8 -*-

"""
This module get informaton from converter.py about what and how data have to be
converted by calling nesessery functions from mapping.py modules. Result is
written into files.
"""
from soft4recieve_write_Rel2.Converter.converter import line_from_file

def main():
    """

    """
    for arg['arg1'], arg['arg2'], arg['arg3'] in line_from_file(sfd):#read data from files
        for fun in func_pool:
            try:
                # Create file's object from function's attribute that stores path to writing file
                func_file = open(fun.my_file,'a')
                func_file.write(fun(**arg)+'')
                func_file.close()
            except:
                # Create file, write head string and first line
                f_test1 = open(fun.__name__ + '.dat','w')
                f_test1.write('This is head of %s\n\n'%fun.__name__)
                f_test1.write(fun(**arg)+'')
                f_test1.close()
                # Attach file's name as function attribute
                fun.__setattr__('my_file' ,fun.__name__ + file_path)
    print 'File name is %s'%fun.my_file

if __name__ == "__main__":
    pass