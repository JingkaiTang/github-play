
#! /usr/bin/env python

def make_eye(str_arg):
    world_or_own_child(str_arg)
    print('early_problem')

def world_or_own_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_eye('same_government')
