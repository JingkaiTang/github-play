
#! /usr/bin/env python

def bad_problem(str_arg):
    big_time(str_arg)
    print('try_child_at_part')

def big_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_problem('first_place')
