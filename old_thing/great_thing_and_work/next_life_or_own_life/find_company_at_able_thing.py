
#! /usr/bin/env python

def big_company(str_arg):
    company(str_arg)
    print('little_person')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_company('use_man_from_place')
