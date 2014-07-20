
#! /usr/bin/env python

def great_thing(str_arg):
    way_and_good_case(str_arg)
    print('bad_part')

def way_and_good_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_thing('last_child')
