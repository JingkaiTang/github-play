
#! /usr/bin/env python

def man_or_man(str_arg):
    point(str_arg)
    print('small_point')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_or_man('tell_bad_year')
