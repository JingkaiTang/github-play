
#! /usr/bin/env python

def child_and_case(str_arg):
    good_eye_or_life(str_arg)
    print('own_case')

def good_eye_or_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_case('eye_or_different_time')
