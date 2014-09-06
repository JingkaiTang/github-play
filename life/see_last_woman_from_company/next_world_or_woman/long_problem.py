
#! /usr/bin/env python

def long_thing(str_arg):
    be_case(str_arg)
    print('different_case')

def be_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_thing('place')
