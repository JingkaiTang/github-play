
#! /usr/bin/env python

def leave_case_on_own_thing(str_arg):
    government(str_arg)
    print('case')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_case_on_own_thing('have_big_work_under_public_thing')
