
#! /usr/bin/env python

def hand(str_arg):
    other_way(str_arg)
    print('bad_place')

def other_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('world')
