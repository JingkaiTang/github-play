
#! /usr/bin/env python

def tell_large_person(str_arg):
    point_or_person(str_arg)
    print('big_case')

def point_or_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_large_person('work')
