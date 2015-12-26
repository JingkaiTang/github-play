
#! /usr/bin/env python

def try_small_government(str_arg):
    other_problem(str_arg)
    print('same_government_and_problem')

def other_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_small_government('company_and_place')
