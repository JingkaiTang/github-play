
#! /usr/bin/env python

def young_work(str_arg):
    few_work(str_arg)
    print('child')

def few_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    young_work('fact')
