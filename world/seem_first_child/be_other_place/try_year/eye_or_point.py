
#! /usr/bin/env python

def point(str_arg):
    problem(str_arg)
    print('child')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('high_year')
