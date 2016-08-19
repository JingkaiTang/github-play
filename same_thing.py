
#! /usr/bin/env python

def different_thing(str_arg):
    eye_or_hand(str_arg)
    print('child')

def eye_or_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_thing('bad_work_or_world')
