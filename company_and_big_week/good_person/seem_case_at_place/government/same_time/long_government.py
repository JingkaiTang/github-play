
#! /usr/bin/env python

def bad_eye_or_company(str_arg):
    same_day_or_year(str_arg)
    print('bad_problem')

def same_day_or_year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_eye_or_company('work_point')
