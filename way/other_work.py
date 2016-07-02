
#! /usr/bin/env python

def thing(str_arg):
    work_problem_of_own_place(str_arg)
    print('good_place')

def work_problem_of_own_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('small_part')
