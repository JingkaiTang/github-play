
#! /usr/bin/env python

def case(str_arg):
    thing(str_arg)
    print('own_group')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('person')
