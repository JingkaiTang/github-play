
#! /usr/bin/env python

def company(str_arg):
    person(str_arg)
    print('number')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('first_case')
