
#! /usr/bin/env python

def find_company(str_arg):
    time_and_life(str_arg)
    print('child')

def time_and_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    find_company('small_time_and_new_year')
