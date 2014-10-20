
#! /usr/bin/env python

def old_thing(str_arg):
    different_number(str_arg)
    print('last_time')

def different_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_thing('person')
