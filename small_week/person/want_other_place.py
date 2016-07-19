
#! /usr/bin/env python

def little_world(str_arg):
    old_child(str_arg)
    print('next_time')

def old_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_world('way_and_number')
