
#! /usr/bin/env python

def different_case(str_arg):
    child(str_arg)
    print('life')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_case('new_day')
