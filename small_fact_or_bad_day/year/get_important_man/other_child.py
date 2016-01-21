
#! /usr/bin/env python

def important_point(str_arg):
    thing(str_arg)
    print('good_child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    important_point('eye')
