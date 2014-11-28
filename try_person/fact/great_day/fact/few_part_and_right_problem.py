
#! /usr/bin/env python

def few_case_or_big_case(str_arg):
    small_case(str_arg)
    print('long_way')

def small_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    few_case_or_big_case('eye_and_time')
