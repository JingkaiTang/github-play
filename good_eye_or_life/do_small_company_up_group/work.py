
#! /usr/bin/env python

def small_child(str_arg):
    large_point(str_arg)
    print('part')

def large_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_child('be_world_on_person')
