
#! /usr/bin/env python

def thing(str_arg):
    say_case(str_arg)
    print('leave_large_child')

def say_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('early_case')
