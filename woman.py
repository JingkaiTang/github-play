
#! /usr/bin/env python

def feel_own_thing(str_arg):
    say_thing_of_other_thing(str_arg)
    print('great_world')

def say_thing_of_other_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    feel_own_thing('use_different_time')
