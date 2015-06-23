
#! /usr/bin/env python

def little_thing(str_arg):
    great_man(str_arg)
    print('problem')

def great_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_thing('place')
