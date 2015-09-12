
#! /usr/bin/env python

def thing(str_arg):
    thing_or_number(str_arg)
    print('woman')

def thing_or_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('man')
