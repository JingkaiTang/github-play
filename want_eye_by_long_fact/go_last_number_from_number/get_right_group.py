
#! /usr/bin/env python

def eye(str_arg):
    group(str_arg)
    print('try_child')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('next_point')
