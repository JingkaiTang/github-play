
#! /usr/bin/env python

def child(str_arg):
    old_number(str_arg)
    print('work_child')

def old_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('world')
