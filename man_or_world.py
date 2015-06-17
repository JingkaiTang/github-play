
#! /usr/bin/env python

def number(str_arg):
    good_thing(str_arg)
    print('child')

def good_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number('first_woman')
