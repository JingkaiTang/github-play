
#! /usr/bin/env python

def child(str_arg):
    child(str_arg)
    print('next_fact')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('work_first_time')
