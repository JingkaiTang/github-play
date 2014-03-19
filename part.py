
#! /usr/bin/env python

def hand(str_arg):
    world(str_arg)
    print('little_point')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('child')
