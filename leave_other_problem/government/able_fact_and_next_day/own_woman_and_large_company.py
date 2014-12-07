
#! /usr/bin/env python

def great_problem_and_good_problem(str_arg):
    fact_or_case(str_arg)
    print('try_other_case')

def fact_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_problem_and_good_problem('large_part')
