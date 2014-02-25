
#! /usr/bin/env python

def small_company(str_arg):
    call_own_group(str_arg)
    print('public_work')

def call_own_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_company('time')
