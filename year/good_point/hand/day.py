
#! /usr/bin/env python

def child(str_arg):
    first_place(str_arg)
    print('group')

def first_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('child')
