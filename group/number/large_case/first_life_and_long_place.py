
#! /usr/bin/env python

def time(str_arg):
    child(str_arg)
    print('time')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time('early_group')
