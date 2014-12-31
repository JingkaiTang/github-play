
#! /usr/bin/env python

def child(str_arg):
    same_world(str_arg)
    print('time')

def same_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('high_fact')
