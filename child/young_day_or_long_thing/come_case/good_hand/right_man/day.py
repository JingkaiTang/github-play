
#! /usr/bin/env python

def world(str_arg):
    other_child(str_arg)
    print('government')

def other_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('take_few_child_above_number')
