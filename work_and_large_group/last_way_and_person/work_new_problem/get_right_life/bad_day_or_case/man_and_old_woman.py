
#! /usr/bin/env python

def do_long_work(str_arg):
    next_part_or_place(str_arg)
    print('good_point')

def next_part_or_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_long_work('important_work_and_point')
