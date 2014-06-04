
#! /usr/bin/env python

def public_fact_and_own_child(str_arg):
    good_thing(str_arg)
    print('man')

def good_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_fact_and_own_child('right_part')
