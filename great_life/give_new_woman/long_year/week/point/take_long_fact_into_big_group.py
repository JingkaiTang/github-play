
#! /usr/bin/env python

def public_thing(str_arg):
    want_life(str_arg)
    print('see_group')

def want_life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_thing('small_woman')
