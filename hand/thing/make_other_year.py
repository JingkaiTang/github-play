
#! /usr/bin/env python

def good_world(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_world('small_fact')
