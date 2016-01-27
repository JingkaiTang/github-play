
#! /usr/bin/env python

def point(str_arg):
    other_fact(str_arg)
    print('child')

def other_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('first_way_or_public_thing')
