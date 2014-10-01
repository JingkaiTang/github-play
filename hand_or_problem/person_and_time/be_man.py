
#! /usr/bin/env python

def child(str_arg):
    large_fact(str_arg)
    print('first_child')

def large_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('see_little_group_from_early_man')
