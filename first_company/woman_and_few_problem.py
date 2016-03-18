
#! /usr/bin/env python

def point(str_arg):
    same_thing(str_arg)
    print('public_problem')

def same_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('different_point')
