
#! /usr/bin/env python

def thing_or_old_time(str_arg):
    public_part_and_man(str_arg)
    print('fact')

def public_part_and_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_or_old_time('large_time')
