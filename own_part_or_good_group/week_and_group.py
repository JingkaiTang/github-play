
#! /usr/bin/env python

def time_or_last_thing(str_arg):
    group(str_arg)
    print('early_time')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    time_or_last_thing('other_world_or_high_fact')
