
#! /usr/bin/env python

def bad_case(str_arg):
    company(str_arg)
    print('man_or_place')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_case('small_number')
