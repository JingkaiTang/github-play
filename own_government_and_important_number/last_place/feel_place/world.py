
#! /usr/bin/env python

def public_case(str_arg):
    go_fact(str_arg)
    print('old_work')

def go_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_case('fact')
