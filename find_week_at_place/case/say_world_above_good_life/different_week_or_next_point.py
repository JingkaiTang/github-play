
#! /usr/bin/env python

def work_hand_of_world(str_arg):
    other_way(str_arg)
    print('thing')

def other_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_hand_of_world('government')
