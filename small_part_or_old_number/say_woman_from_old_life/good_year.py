
#! /usr/bin/env python

def child(str_arg):
    same_place(str_arg)
    print('child')

def same_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('be_problem_on_little_group')
