
#! /usr/bin/env python

def public_work(str_arg):
    same_case(str_arg)
    print('person')

def same_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_work('number')
