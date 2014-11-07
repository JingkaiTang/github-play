
#! /usr/bin/env python

def long_work_or_hand(str_arg):
    first_man(str_arg)
    print('woman')

def first_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_work_or_hand('use_work')
