
#! /usr/bin/env python

def thing(str_arg):
    person(str_arg)
    print('good_child')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('know_number')
