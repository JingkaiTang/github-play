
#! /usr/bin/env python

def person(str_arg):
    child(str_arg)
    print('child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('other_life')
