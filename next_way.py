
#! /usr/bin/env python

def man(str_arg):
    have_eye(str_arg)
    print('child')

def have_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('big_work')
