
#! /usr/bin/env python

def child(str_arg):
    point(str_arg)
    print('number')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('year')
