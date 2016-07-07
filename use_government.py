
#! /usr/bin/env python

def make_other_child_after_case(str_arg):
    child(str_arg)
    print('problem')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_other_child_after_case('different_child')
