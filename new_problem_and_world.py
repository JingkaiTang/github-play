
#! /usr/bin/env python

def child(str_arg):
    man(str_arg)
    print('last_hand')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('try_number_to_public_place')
