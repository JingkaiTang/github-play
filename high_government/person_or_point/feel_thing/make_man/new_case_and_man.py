
#! /usr/bin/env python

def call_same_point_at_child(str_arg):
    work_person(str_arg)
    print('problem')

def work_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_same_point_at_child('have_old_life')
