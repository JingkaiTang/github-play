
#! /usr/bin/env python

def child(str_arg):
    way(str_arg)
    print('good_group')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('fact')
