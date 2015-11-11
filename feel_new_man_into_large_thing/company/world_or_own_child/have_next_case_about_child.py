
#! /usr/bin/env python

def first_day(str_arg):
    go_child(str_arg)
    print('go_place_from_next_child')

def go_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_day('high_number')
