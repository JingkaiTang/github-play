
#! /usr/bin/env python

def child(str_arg):
    way(str_arg)
    print('own_time_and_child')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('little_fact')
