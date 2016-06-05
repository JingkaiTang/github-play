
#! /usr/bin/env python

def other_work(str_arg):
    able_week(str_arg)
    print('child')

def able_week(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_work('child')
