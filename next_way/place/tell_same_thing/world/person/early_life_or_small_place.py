
#! /usr/bin/env python

def world(str_arg):
    long_number(str_arg)
    print('child')

def long_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('fact_and_government')
