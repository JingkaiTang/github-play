
#! /usr/bin/env python

def try_own_thing(str_arg):
    woman_and_little_way(str_arg)
    print('different_thing')

def woman_and_little_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_own_thing('new_thing_or_woman')
