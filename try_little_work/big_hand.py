
#! /usr/bin/env python

def little_woman(str_arg):
    take_different_hand_in_case(str_arg)
    print('man')

def take_different_hand_in_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_woman('case_and_last_work')
