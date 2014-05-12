
#! /usr/bin/env python

def new_way(str_arg):
    last_world_and_child(str_arg)
    print('public_way')

def last_world_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_way('way_and_man')
