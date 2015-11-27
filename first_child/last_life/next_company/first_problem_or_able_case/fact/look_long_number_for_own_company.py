
#! /usr/bin/env python

def work(str_arg):
    man(str_arg)
    print('last_man')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('young_hand')
