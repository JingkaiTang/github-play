
#! /usr/bin/env python

def small_time(str_arg):
    government(str_arg)
    print('large_part')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_time('long_point')
