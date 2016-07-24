
#! /usr/bin/env python

def next_hand(str_arg):
    own_number_and_small_work(str_arg)
    print('take_right_hand')

def own_number_and_small_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    next_hand('own_day')
