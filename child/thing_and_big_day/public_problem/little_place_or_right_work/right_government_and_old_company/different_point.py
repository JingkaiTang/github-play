
#! /usr/bin/env python

def bad_eye(str_arg):
    big_part(str_arg)
    print('important_problem')

def big_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_eye('find_same_time_by_early_person')
