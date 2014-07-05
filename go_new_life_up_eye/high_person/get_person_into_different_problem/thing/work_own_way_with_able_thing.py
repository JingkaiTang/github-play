
#! /usr/bin/env python

def different_way(str_arg):
    bad_problem_or_next_case(str_arg)
    print('other_case')

def bad_problem_or_next_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_way('fact')
