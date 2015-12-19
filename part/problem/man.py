
#! /usr/bin/env python

def bad_child(str_arg):
    want_group(str_arg)
    print('right_part')

def want_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_child('thing')
