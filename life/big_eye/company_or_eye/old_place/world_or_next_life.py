
#! /usr/bin/env python

def long_child(str_arg):
    year(str_arg)
    print('last_child')

def year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    long_child('ask_old_hand')
