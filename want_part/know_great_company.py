
#! /usr/bin/env python

def say_thing(str_arg):
    world(str_arg)
    print('week')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_thing('life')
