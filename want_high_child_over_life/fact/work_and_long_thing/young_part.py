
#! /usr/bin/env python

def work(str_arg):
    child(str_arg)
    print('few_thing')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('woman')
