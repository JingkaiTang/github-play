
#! /usr/bin/env python

def person(str_arg):
    ask_world_with_small_man(str_arg)
    print('public_child')

def ask_world_with_small_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('able_person')
