
#! /usr/bin/env python

def other_work(str_arg):
    old_thing(str_arg)
    print('public_group')

def old_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_work('little_child')
