
#! /usr/bin/env python

def last_thing(str_arg):
    say_world_on_last_thing(str_arg)
    print('little_thing')

def say_world_on_last_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    last_thing('see_week')
