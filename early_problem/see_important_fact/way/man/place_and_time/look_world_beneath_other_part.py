
#! /usr/bin/env python

def child_and_company(str_arg):
    long_company(str_arg)
    print('time')

def long_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_company('get_day')
