
#! /usr/bin/env python

def part_or_large_hand(str_arg):
    try_little_eye(str_arg)
    print('big_hand')

def try_little_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    part_or_large_hand('little_thing')
