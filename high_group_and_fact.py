
#! /usr/bin/env python

def old_child(str_arg):
    world(str_arg)
    print('public_way')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_child('come_own_year_of_hand')
