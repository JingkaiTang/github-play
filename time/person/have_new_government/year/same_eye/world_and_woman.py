
#! /usr/bin/env python

def man(str_arg):
    child(str_arg)
    print('number_and_year')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('high_number_and_small_day')
