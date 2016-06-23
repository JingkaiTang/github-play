
#! /usr/bin/env python

def bad_problem(str_arg):
    new_fact_and_part(str_arg)
    print('call_few_problem_in_child')

def new_fact_and_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_problem('first_man')
