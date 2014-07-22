
#! /usr/bin/env python

def call_same_eye(str_arg):
    problem(str_arg)
    print('child')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_same_eye('year_and_fact')
