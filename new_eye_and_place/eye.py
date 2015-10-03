
#! /usr/bin/env python

def life(str_arg):
    long_place(str_arg)
    print('child')

def long_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('number_and_company')
