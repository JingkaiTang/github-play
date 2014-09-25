
#! /usr/bin/env python

def bad_place(str_arg):
    thing(str_arg)
    print('work')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_place('make_public_problem_to_week')
