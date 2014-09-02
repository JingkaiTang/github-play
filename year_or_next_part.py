
#! /usr/bin/env python

def thing_or_small_hand(str_arg):
    go_hand(str_arg)
    print('long_part')

def go_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_or_small_hand('find_big_work_at_world')
