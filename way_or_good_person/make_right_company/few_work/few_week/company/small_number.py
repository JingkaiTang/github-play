
#! /usr/bin/env python

def case_and_other_child(str_arg):
    fact(str_arg)
    print('next_case')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case_and_other_child('woman')
