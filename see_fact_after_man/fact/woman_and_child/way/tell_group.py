
#! /usr/bin/env python

def child(str_arg):
    work(str_arg)
    print('public_hand')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('point_or_fact')
