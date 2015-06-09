
#! /usr/bin/env python

def child(str_arg):
    next_thing(str_arg)
    print('problem')

def next_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('life_and_man')
