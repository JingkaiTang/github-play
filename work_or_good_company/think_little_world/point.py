
#! /usr/bin/env python

def first_case(str_arg):
    child(str_arg)
    print('tell_other_group')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_case('year')
