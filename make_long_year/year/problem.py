
#! /usr/bin/env python

def leave_woman(str_arg):
    tell_hand(str_arg)
    print('new_day')

def tell_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_woman('person')
