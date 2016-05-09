
#! /usr/bin/env python

def see_man_in_place(str_arg):
    leave_own_part_with_bad_place(str_arg)
    print('large_problem')

def leave_own_part_with_bad_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_man_in_place('own_way')
