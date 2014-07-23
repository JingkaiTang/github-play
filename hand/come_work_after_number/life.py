
#! /usr/bin/env python

def bad_place(str_arg):
    number(str_arg)
    print('long_child_or_number')

def number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_place('few_case_and_next_day')
