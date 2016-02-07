
#! /usr/bin/env python

def find_point_under_fact(str_arg):
    work(str_arg)
    print('child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    find_point_under_fact('bad_fact_or_old_place')
