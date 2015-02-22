
#! /usr/bin/env python

def hand(str_arg):
    public_part(str_arg)
    print('right_number')

def public_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('leave_good_group')
