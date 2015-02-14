
#! /usr/bin/env python

def want_life(str_arg):
    work(str_arg)
    print('important_child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_life('woman_and_early_part')
