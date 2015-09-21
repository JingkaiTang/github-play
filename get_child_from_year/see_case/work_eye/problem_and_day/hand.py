
#! /usr/bin/env python

def child(str_arg):
    good_world(str_arg)
    print('way_or_long_time')

def good_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('thing')
