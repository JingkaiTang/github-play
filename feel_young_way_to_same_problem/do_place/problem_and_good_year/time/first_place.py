
#! /usr/bin/env python

def use_problem_by_thing(str_arg):
    bad_world(str_arg)
    print('do_important_number_about_bad_world')

def bad_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_problem_by_thing('point_and_year')
