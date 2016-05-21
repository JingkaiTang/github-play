
#! /usr/bin/env python

def long_problem(str_arg):
    big_way(str_arg)
    print('small_case')

def big_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_problem('find_large_person')
