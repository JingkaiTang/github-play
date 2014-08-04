
#! /usr/bin/env python

def tell_right_way(str_arg):
    day(str_arg)
    print('year')

def day(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_right_way('other_part')
