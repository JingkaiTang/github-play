
#! /usr/bin/env python

def life(str_arg):
    life_and_child(str_arg)
    print('child')

def life_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life('hand_and_right_woman')
