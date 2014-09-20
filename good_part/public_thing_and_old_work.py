
#! /usr/bin/env python

def early_thing(str_arg):
    work(str_arg)
    print('eye')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_thing('hand_or_world')
