
#! /usr/bin/env python

def child(str_arg):
    own_part_and_child(str_arg)
    print('important_thing')

def own_part_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('group')
