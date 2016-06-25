
#! /usr/bin/env python

def child(str_arg):
    high_number(str_arg)
    print('good_point')

def high_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('new_case_or_group')
