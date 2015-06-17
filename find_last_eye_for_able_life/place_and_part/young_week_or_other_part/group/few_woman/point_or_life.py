
#! /usr/bin/env python

def early_thing(str_arg):
    next_group(str_arg)
    print('bad_part')

def next_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_thing('child')
