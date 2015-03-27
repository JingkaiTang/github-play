
#! /usr/bin/env python

def company(str_arg):
    group_or_old_year(str_arg)
    print('do_child')

def group_or_old_year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company('young_woman')
