
#! /usr/bin/env python

def big_way_and_world(str_arg):
    big_eye(str_arg)
    print('child')

def big_eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_way_and_world('great_man')
