
#! /usr/bin/env python

def problem_and_case(str_arg):
    child(str_arg)
    print('new_number')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem_and_case('first_point')
