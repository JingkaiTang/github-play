
#! /usr/bin/env python

def early_case(str_arg):
    person(str_arg)
    print('thing')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_case('point_or_high_case')
