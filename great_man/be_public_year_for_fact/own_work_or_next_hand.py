
#! /usr/bin/env python

def thing(str_arg):
    good_point(str_arg)
    print('first_way')

def good_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('number')
