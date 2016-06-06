
#! /usr/bin/env python

def little_part(str_arg):
    big_part(str_arg)
    print('company')

def big_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_part('next_time')
