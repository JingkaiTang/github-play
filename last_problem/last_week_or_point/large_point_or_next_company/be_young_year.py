
#! /usr/bin/env python

def other_group(str_arg):
    good_child(str_arg)
    print('group_or_early_case')

def good_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_group('bad_day')
