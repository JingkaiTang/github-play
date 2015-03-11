
#! /usr/bin/env python

def world(str_arg):
    number(str_arg)
    print('have_number')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('have_last_work')
