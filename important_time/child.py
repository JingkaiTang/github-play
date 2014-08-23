
#! /usr/bin/env python

def company(str_arg):
    person(str_arg)
    print('person')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('first_world_or_way')
