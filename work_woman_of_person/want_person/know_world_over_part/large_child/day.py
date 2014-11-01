
#! /usr/bin/env python

def bad_point(str_arg):
    tell_small_point(str_arg)
    print('same_person')

def tell_small_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_point('right_thing')
