
#! /usr/bin/env python

def work(str_arg):
    eye(str_arg)
    print('child')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('day_and_first_eye')
