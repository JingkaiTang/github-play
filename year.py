
#! /usr/bin/env python

def do_bad_case_in_own_place(str_arg):
    child_and_child(str_arg)
    print('make_public_day')

def child_and_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_bad_case_in_own_place('number')
