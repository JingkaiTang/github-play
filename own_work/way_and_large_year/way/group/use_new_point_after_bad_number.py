
#! /usr/bin/env python

def long_number(str_arg):
    bad_way(str_arg)
    print('problem')

def bad_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_number('make_life')
