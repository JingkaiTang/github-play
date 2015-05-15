
#! /usr/bin/env python

def point(str_arg):
    big_part(str_arg)
    print('child')

def big_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('public_group')
