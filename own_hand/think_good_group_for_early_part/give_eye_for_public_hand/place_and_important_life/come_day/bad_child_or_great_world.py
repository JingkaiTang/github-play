
#! /usr/bin/env python

def important_thing(str_arg):
    same_man(str_arg)
    print('small_thing')

def same_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_thing('little_group')
