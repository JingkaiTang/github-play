
#! /usr/bin/env python

def take_time(str_arg):
    point_or_big_child(str_arg)
    print('good_child')

def point_or_big_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_time('take_early_place')
