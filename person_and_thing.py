
#! /usr/bin/env python

def large_case(str_arg):
    small_case(str_arg)
    print('new_woman')

def small_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_case('case')
