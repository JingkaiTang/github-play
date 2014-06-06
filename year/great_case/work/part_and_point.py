
#! /usr/bin/env python

def bad_group(str_arg):
    different_man(str_arg)
    print('child')

def different_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_group('last_thing')
