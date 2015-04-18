
#! /usr/bin/env python

def work(str_arg):
    right_number(str_arg)
    print('be_public_child')

def right_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('life')
