
#! /usr/bin/env python

def call_week(str_arg):
    man(str_arg)
    print('first_man')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_week('other_group')
