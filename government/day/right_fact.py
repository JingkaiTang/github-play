
#! /usr/bin/env python

def take_government(str_arg):
    man(str_arg)
    print('woman')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_government('few_world')
