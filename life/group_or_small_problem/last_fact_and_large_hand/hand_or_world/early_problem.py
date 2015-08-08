
#! /usr/bin/env python

def place(str_arg):
    man(str_arg)
    print('other_child')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place('life')
