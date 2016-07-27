
#! /usr/bin/env python

def large_child(str_arg):
    person(str_arg)
    print('same_child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_child('high_fact')
