
#! /usr/bin/env python

def good_world(str_arg):
    bad_place(str_arg)
    print('small_point')

def bad_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_world('eye_or_important_problem')
