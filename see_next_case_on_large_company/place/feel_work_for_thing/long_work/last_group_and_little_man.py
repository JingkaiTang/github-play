
#! /usr/bin/env python

def new_place(str_arg):
    person(str_arg)
    print('child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_place('small_life')
