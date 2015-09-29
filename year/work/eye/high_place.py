
#! /usr/bin/env python

def world(str_arg):
    child(str_arg)
    print('own_life')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('year')
