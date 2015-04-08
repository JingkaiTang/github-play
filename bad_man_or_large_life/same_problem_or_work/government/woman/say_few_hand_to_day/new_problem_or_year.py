
#! /usr/bin/env python

def thing(str_arg):
    point(str_arg)
    print('own_hand')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('next_life')
