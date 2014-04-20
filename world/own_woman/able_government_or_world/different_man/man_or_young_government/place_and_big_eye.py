
#! /usr/bin/env python

def fact_and_person(str_arg):
    do_good_child(str_arg)
    print('public_number')

def do_good_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact_and_person('bad_fact')
