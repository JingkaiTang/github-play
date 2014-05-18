
#! /usr/bin/env python

def leave_own_problem(str_arg):
    work(str_arg)
    print('work_or_place')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_own_problem('number')
