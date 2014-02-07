
#! /usr/bin/env python

def call_week(str_arg):
    do_same_child(str_arg)
    print('public_case')

def do_same_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_week('big_week_or_fact')
