
#! /usr/bin/env python

def try_thing(str_arg):
    bad_day(str_arg)
    print('try_important_thing')

def bad_day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_thing('different_number')
