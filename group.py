
#! /usr/bin/env python

def bad_part(str_arg):
    child(str_arg)
    print('first_world')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_part('think_life')
