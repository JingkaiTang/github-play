
#! /usr/bin/env python

def give_own_world_of_number(str_arg):
    fact(str_arg)
    print('early_child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    give_own_world_of_number('part_and_fact')
