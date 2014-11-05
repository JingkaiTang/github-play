
#! /usr/bin/env python

def child(str_arg):
    long_group(str_arg)
    print('world')

def long_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('person')
