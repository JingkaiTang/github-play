
#! /usr/bin/env python

def own_life(str_arg):
    try_world_with_early_work(str_arg)
    print('child')

def try_world_with_early_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_life('do_thing_at_own_company')
