
#! /usr/bin/env python

def own_life(str_arg):
    good_man(str_arg)
    print('ask_world')

def good_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_life('man')
