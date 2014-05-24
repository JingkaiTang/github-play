
#! /usr/bin/env python

def next_man(str_arg):
    place(str_arg)
    print('child')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    next_man('find_other_fact_to_fact')
