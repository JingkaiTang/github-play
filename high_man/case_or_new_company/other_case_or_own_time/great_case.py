
#! /usr/bin/env python

def child(str_arg):
    problem(str_arg)
    print('use_small_problem')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('other_week')
