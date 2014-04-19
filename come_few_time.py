
#! /usr/bin/env python

def other_case(str_arg):
    number(str_arg)
    print('public_hand')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_case('week')
