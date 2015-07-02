
#! /usr/bin/env python

def right_work(str_arg):
    high_child(str_arg)
    print('high_hand')

def high_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    right_work('large_fact_and_little_child')
