
#! /usr/bin/env python

def world_or_work(str_arg):
    other_thing(str_arg)
    print('man')

def other_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_work('woman')
