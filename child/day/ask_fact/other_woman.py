
#! /usr/bin/env python

def public_man(str_arg):
    new_way(str_arg)
    print('next_thing')

def new_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_man('same_time_and_fact')
