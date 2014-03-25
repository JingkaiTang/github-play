
#! /usr/bin/env python

def tell_long_group_for_group(str_arg):
    group(str_arg)
    print('man')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_long_group_for_group('bad_day')
