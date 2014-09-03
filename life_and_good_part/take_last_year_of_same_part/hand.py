
#! /usr/bin/env python

def call_government(str_arg):
    big_work(str_arg)
    print('world')

def big_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_government('eye')
