
#! /usr/bin/env python

def woman(str_arg):
    man(str_arg)
    print('bad_world')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('same_way')
