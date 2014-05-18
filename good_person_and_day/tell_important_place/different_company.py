
#! /usr/bin/env python

def good_day(str_arg):
    world(str_arg)
    print('right_world')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_day('work_large_person_at_big_world')
