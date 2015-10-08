
#! /usr/bin/env python

def want_small_time(str_arg):
    world(str_arg)
    print('other_child')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_small_time('man')
