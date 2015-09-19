
#! /usr/bin/env python

def good_way(str_arg):
    say_group(str_arg)
    print('eye')

def say_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_way('long_part')
