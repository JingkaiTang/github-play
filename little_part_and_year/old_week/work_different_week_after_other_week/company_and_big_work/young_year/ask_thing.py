
#! /usr/bin/env python

def work_new_problem_by_own_child(str_arg):
    number(str_arg)
    print('bad_child')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_new_problem_by_own_child('world')
