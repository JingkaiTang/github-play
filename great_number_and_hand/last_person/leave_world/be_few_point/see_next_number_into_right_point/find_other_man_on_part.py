
#! /usr/bin/env python

def man(str_arg):
    person(str_arg)
    print('eye')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('woman')
