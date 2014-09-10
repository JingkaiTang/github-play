
#! /usr/bin/env python

def child(str_arg):
    case_and_different_child(str_arg)
    print('say_case')

def case_and_different_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('old_hand')
