
#! /usr/bin/env python

def child(str_arg):
    hand(str_arg)
    print('do_own_company')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('first_child')
