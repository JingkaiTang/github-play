
#! /usr/bin/env python

def other_person(str_arg):
    big_way(str_arg)
    print('child')

def big_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_person('fact_or_right_hand')
