
#! /usr/bin/env python

def have_point(str_arg):
    work(str_arg)
    print('different_number')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    have_point('world')
