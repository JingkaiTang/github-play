
#! /usr/bin/env python

def world(str_arg):
    man(str_arg)
    print('own_world')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('next_world')
