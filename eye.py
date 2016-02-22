
#! /usr/bin/env python

def problem(str_arg):
    new_problem(str_arg)
    print('early_problem')

def new_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('small_man')
