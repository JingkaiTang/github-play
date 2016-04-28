
#! /usr/bin/env python

def woman(str_arg):
    man(str_arg)
    print('work')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('problem')
