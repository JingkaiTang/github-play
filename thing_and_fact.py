
#! /usr/bin/env python

def say_own_case(str_arg):
    government(str_arg)
    print('person')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_own_case('have_case')
