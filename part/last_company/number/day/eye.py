
#! /usr/bin/env python

def child_or_work(str_arg):
    old_man(str_arg)
    print('fact')

def old_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_work('next_company')
