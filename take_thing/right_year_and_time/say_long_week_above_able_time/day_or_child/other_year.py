
#! /usr/bin/env python

def little_problem(str_arg):
    child(str_arg)
    print('look_bad_problem')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_problem('own_fact')
