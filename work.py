
#! /usr/bin/env python

def tell_child_to_place(str_arg):
    time(str_arg)
    print('life')

def time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_child_to_place('bad_problem')
