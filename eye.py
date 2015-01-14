
#! /usr/bin/env python

def group(str_arg):
    case(str_arg)
    print('do_own_group')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    group('same_hand_and_woman')
