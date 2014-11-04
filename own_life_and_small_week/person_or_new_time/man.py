
#! /usr/bin/env python

def place(str_arg):
    get_own_child(str_arg)
    print('own_part_or_long_case')

def get_own_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place('week')
