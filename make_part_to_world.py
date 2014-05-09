
#! /usr/bin/env python

def long_child(str_arg):
    thing(str_arg)
    print('person')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_child('man')
