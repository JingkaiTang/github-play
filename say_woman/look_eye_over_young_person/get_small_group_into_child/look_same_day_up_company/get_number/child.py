
#! /usr/bin/env python

def small_thing(str_arg):
    long_life(str_arg)
    print('leave_same_work')

def long_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_thing('great_world_or_own_problem')
