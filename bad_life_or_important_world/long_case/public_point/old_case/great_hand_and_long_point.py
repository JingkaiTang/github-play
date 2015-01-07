
#! /usr/bin/env python

def do_thing_over_small_part(str_arg):
    group(str_arg)
    print('group')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_thing_over_small_part('case')
