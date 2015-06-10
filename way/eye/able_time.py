
#! /usr/bin/env python

def man(str_arg):
    next_man(str_arg)
    print('hand')

def next_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('same_thing_or_large_thing')
