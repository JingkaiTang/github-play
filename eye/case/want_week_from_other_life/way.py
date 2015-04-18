
#! /usr/bin/env python

def thing(str_arg):
    small_part_and_own_fact(str_arg)
    print('number')

def small_part_and_own_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('child')
