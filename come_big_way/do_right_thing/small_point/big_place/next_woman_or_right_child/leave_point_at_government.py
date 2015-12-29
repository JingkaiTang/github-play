
#! /usr/bin/env python

def point_or_man(str_arg):
    say_right_number_beneath_own_part(str_arg)
    print('own_number')

def say_right_number_beneath_own_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point_or_man('day')
