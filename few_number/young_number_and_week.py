
#! /usr/bin/env python

def child_or_man(str_arg):
    group(str_arg)
    print('part')

def group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_man('be_long_day')
