
#! /usr/bin/env python

def place(str_arg):
    thing(str_arg)
    print('place')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place('person')
