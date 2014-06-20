
#! /usr/bin/env python

def other_man(str_arg):
    old_way(str_arg)
    print('long_time_and_year')

def old_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_man('group')
