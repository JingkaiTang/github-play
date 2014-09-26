
#! /usr/bin/env python

def next_hand_or_problem(str_arg):
    problem(str_arg)
    print('hand')

def problem(str_arg):
    print(str_arg)

if __name__ == '__main__':
    next_hand_or_problem('group')
