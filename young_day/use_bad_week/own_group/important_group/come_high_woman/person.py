
#! /usr/bin/env python

def big_work(str_arg):
    thing_or_part(str_arg)
    print('work')

def thing_or_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_work('company')
