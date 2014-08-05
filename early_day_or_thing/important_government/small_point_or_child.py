
#! /usr/bin/env python

def little_world(str_arg):
    point(str_arg)
    print('last_child')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_world('number')
