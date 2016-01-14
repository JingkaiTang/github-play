
#! /usr/bin/env python

def work(str_arg):
    old_child(str_arg)
    print('early_thing')

def old_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('person')
