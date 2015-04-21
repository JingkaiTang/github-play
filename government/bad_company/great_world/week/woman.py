
#! /usr/bin/env python

def leave_way(str_arg):
    small_eye_or_next_group(str_arg)
    print('eye')

def small_eye_or_next_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_way('hand')
