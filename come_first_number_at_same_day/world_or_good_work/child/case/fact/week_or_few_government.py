
#! /usr/bin/env python

def high_thing(str_arg):
    child(str_arg)
    print('big_group_or_fact')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    high_thing('long_year')
