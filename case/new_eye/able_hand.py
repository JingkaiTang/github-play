
#! /usr/bin/env python

def own_point(str_arg):
    small_child(str_arg)
    print('different_case_and_world')

def small_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_point('year')
