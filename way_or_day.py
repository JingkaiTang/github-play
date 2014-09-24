
#! /usr/bin/env python

def ask_different_case(str_arg):
    child(str_arg)
    print('place')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    ask_different_case('high_case')
