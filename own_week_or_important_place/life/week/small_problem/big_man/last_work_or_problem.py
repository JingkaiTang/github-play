
#! /usr/bin/env python

def public_life(str_arg):
    life(str_arg)
    print('little_fact')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_life('group_or_good_problem')
