
#! /usr/bin/env python

def see_life(str_arg):
    person(str_arg)
    print('group')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_life('week')
