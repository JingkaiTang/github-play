
#! /usr/bin/env python

def problem(str_arg):
    child(str_arg)
    print('other_work')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    problem('life')
