
#! /usr/bin/env python

def life(str_arg):
    child(str_arg)
    print('long_time')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('company')
