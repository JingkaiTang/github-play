
#! /usr/bin/env python

def child(str_arg):
    part(str_arg)
    print('child')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('thing')
