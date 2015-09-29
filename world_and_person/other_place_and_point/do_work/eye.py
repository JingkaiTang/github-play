
#! /usr/bin/env python

def problem(str_arg):
    high_fact(str_arg)
    print('call_child_at_first_problem')

def high_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('old_child_and_woman')
