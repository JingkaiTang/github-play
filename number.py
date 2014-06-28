
#! /usr/bin/env python

def small_problem(str_arg):
    hand_or_different_number(str_arg)
    print('other_case')

def hand_or_different_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_problem('last_time')
