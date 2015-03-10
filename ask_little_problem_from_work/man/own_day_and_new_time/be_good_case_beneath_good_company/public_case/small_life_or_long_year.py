
#! /usr/bin/env python

def world_or_case(str_arg):
    part(str_arg)
    print('public_child')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_case('eye')
