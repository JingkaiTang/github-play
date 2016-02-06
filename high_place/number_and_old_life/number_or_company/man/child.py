
#! /usr/bin/env python

def number_and_world(str_arg):
    bad_place(str_arg)
    print('call_hand')

def bad_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number_and_world('different_year')
