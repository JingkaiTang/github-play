
#! /usr/bin/env python

def work(str_arg):
    good_day(str_arg)
    print('public_thing')

def good_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('little_point_or_large_group')
