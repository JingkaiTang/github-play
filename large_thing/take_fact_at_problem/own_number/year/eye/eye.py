
#! /usr/bin/env python

def thing(str_arg):
    man(str_arg)
    print('child')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('old_year_or_way')
