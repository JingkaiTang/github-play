
#! /usr/bin/env python

def tell_last_world_above_big_work(str_arg):
    tell_world(str_arg)
    print('next_way')

def tell_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_last_world_above_big_work('early_man')
