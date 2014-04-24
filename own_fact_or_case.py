
#! /usr/bin/env python

def same_case(str_arg):
    old_thing(str_arg)
    print('same_case')

def old_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_case('point')
