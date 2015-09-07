
#! /usr/bin/env python

def person(str_arg):
    call_problem_on_last_thing(str_arg)
    print('good_way')

def call_problem_on_last_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('do_long_day_in_different_company')
