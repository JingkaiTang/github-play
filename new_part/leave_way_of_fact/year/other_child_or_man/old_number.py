
#! /usr/bin/env python

def see_public_way(str_arg):
    man(str_arg)
    print('problem')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_public_way('large_thing')
