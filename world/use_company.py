
#! /usr/bin/env python

def problem_or_different_work(str_arg):
    man(str_arg)
    print('problem')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem_or_different_work('company')
