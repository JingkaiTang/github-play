
#! /usr/bin/env python

def call_last_man(str_arg):
    person(str_arg)
    print('group_and_hand')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_last_man('world')
