
#! /usr/bin/env python

def child_or_bad_work(str_arg):
    number_and_place(str_arg)
    print('place')

def number_and_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_bad_work('go_part_by_point')
