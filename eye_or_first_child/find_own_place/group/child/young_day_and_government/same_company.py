
#! /usr/bin/env python

def call_own_child_above_same_part(str_arg):
    week_and_problem(str_arg)
    print('make_group')

def week_and_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_own_child_above_same_part('other_problem_and_case')
