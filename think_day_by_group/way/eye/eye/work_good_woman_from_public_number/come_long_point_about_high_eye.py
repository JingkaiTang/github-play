
#! /usr/bin/env python

def think_hand(str_arg):
    hand_or_child(str_arg)
    print('old_way')

def hand_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    think_hand('way_or_point')
