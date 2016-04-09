
#! /usr/bin/env python

def give_child(str_arg):
    public_hand(str_arg)
    print('public_thing')

def public_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    give_child('big_fact')
