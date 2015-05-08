
#! /usr/bin/env python

def work(str_arg):
    big_thing(str_arg)
    print('bad_place')

def big_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('big_point_and_own_point')
