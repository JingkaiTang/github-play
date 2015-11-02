
#! /usr/bin/env python

def high_life(str_arg):
    point_or_man(str_arg)
    print('child')

def point_or_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    high_life('time')
