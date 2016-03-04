
#! /usr/bin/env python

def child(str_arg):
    last_number(str_arg)
    print('group')

def last_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('different_part_or_new_week')
