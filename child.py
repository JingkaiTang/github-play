
#! /usr/bin/env python

def child(str_arg):
    own_problem(str_arg)
    print('group')

def own_problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('group')
