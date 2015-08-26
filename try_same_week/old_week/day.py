
#! /usr/bin/env python

def company(str_arg):
    big_child(str_arg)
    print('world')

def big_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('woman')
