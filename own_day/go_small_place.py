
#! /usr/bin/env python

def large_world(str_arg):
    child(str_arg)
    print('person_and_big_child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    large_world('man')
