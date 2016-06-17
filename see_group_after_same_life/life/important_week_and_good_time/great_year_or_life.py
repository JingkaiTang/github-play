
#! /usr/bin/env python

def other_eye(str_arg):
    right_thing(str_arg)
    print('high_world_and_right_world')

def right_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_eye('child')
