
#! /usr/bin/env python

def different_world(str_arg):
    different_child(str_arg)
    print('long_man')

def different_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_world('come_place')
