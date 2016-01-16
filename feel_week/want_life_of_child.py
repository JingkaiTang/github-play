
#! /usr/bin/env python

def come_child(str_arg):
    large_world(str_arg)
    print('new_man_or_world')

def large_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    come_child('hand')
