
#! /usr/bin/env python

def tell_time(str_arg):
    early_thing_or_child(str_arg)
    print('long_time')

def early_thing_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_time('group')
