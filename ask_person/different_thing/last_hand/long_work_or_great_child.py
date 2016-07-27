
#! /usr/bin/env python

def woman(str_arg):
    child(str_arg)
    print('important_thing')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('problem')
