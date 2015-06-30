
#! /usr/bin/env python

def child_or_problem(str_arg):
    ask_new_person(str_arg)
    print('public_group')

def ask_new_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_problem('last_problem')
