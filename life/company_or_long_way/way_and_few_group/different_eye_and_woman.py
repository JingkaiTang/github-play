
#! /usr/bin/env python

def hand_and_next_company(str_arg):
    hand(str_arg)
    print('right_time')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand_and_next_company('time')
