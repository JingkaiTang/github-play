
#! /usr/bin/env python

def long_world(str_arg):
    part(str_arg)
    print('public_case')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_world('thing')
