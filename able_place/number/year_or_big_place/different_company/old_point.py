
#! /usr/bin/env python

def hand(str_arg):
    world(str_arg)
    print('new_group')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('place_and_child')
