
#! /usr/bin/env python

def thing(str_arg):
    good_number_and_way(str_arg)
    print('bad_place')

def good_number_and_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('big_hand')
