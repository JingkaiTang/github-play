
#! /usr/bin/env python

def time(str_arg):
    old_child_or_case(str_arg)
    print('new_part')

def old_child_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('world')
