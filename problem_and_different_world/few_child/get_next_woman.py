
#! /usr/bin/env python

def woman(str_arg):
    public_woman(str_arg)
    print('right_fact')

def public_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('want_child_beneath_year')
