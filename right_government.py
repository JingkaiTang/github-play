
#! /usr/bin/env python

def bad_way_and_man(str_arg):
    leave_important_part_into_first_week(str_arg)
    print('life')

def leave_important_part_into_first_week(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_way_and_man('public_place')
