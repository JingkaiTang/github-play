
#! /usr/bin/env python

def make_problem(str_arg):
    use_case_above_part(str_arg)
    print('have_next_part')

def use_case_above_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_problem('bad_year')
