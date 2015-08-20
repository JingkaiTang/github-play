
#! /usr/bin/env python

def problem(str_arg):
    child(str_arg)
    print('leave_important_world')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('public_place')
