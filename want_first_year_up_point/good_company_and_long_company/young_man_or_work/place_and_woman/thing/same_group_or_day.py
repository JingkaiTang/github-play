
#! /usr/bin/env python

def small_work(str_arg):
    little_work(str_arg)
    print('child_or_right_group')

def little_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    small_work('different_part')
