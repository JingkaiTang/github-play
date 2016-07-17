
#! /usr/bin/env python

def fact(str_arg):
    group(str_arg)
    print('child')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('week')
