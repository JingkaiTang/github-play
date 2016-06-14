
#! /usr/bin/env python

def bad_part(str_arg):
    work(str_arg)
    print('same_fact_and_different_case')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_part('use_company')
