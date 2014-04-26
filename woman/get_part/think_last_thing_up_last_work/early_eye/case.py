
#! /usr/bin/env python

def other_child(str_arg):
    point_or_part(str_arg)
    print('fact_or_large_life')

def point_or_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('say_time')
