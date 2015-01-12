
#! /usr/bin/env python

def work_child(str_arg):
    long_person(str_arg)
    print('number_or_point')

def long_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_child('next_case_and_big_number')
