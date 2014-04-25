
#! /usr/bin/env python

def fact(str_arg):
    make_small_child(str_arg)
    print('different_group')

def make_small_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('large_hand')
