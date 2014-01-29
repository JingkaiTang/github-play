
#! /usr/bin/env python

def hand(str_arg):
    public_fact(str_arg)
    print('public_group')

def public_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('old_number')
