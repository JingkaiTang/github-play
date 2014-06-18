
#! /usr/bin/env python

def do_first_world(str_arg):
    large_day(str_arg)
    print('child')

def large_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_first_world('group')
