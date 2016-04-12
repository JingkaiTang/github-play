
#! /usr/bin/env python

def thing(str_arg):
    take_man(str_arg)
    print('world_or_child')

def take_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('last_fact')
