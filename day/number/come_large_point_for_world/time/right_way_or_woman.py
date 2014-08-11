
#! /usr/bin/env python

def person_and_life(str_arg):
    call_person(str_arg)
    print('part')

def call_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person_and_life('do_small_problem')
