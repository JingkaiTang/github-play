
#! /usr/bin/env python

def next_group(str_arg):
    work(str_arg)
    print('group')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    next_group('new_child')
