
#! /usr/bin/env python

def see_child(str_arg):
    old_problem(str_arg)
    print('big_problem')

def old_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_child('day')
