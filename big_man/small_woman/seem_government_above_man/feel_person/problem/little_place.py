
#! /usr/bin/env python

def same_life(str_arg):
    child(str_arg)
    print('other_point_or_part')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_life('own_world')
