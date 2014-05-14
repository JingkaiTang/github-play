
#! /usr/bin/env python

def child(str_arg):
    group_or_able_child(str_arg)
    print('large_child')

def group_or_able_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('first_child_and_early_point')
