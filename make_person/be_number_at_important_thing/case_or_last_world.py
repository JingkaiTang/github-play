
#! /usr/bin/env python

def little_eye(str_arg):
    call_big_time_with_world(str_arg)
    print('early_eye')

def call_big_time_with_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_eye('feel_part')
