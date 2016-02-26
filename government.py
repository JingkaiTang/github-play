
#! /usr/bin/env python

def say_first_thing_by_good_person(str_arg):
    point_and_life(str_arg)
    print('public_world')

def point_and_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_first_thing_by_good_person('different_life_and_number')
