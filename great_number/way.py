
#! /usr/bin/env python

def big_work(str_arg):
    old_point(str_arg)
    print('old_fact')

def old_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('year')
