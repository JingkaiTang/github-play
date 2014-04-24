
#! /usr/bin/env python

def find_public_thing(str_arg):
    person(str_arg)
    print('eye')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    find_public_thing('old_way')
