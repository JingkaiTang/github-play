
#! /usr/bin/env python

def child(str_arg):
    tell_thing(str_arg)
    print('part')

def tell_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('young_part')
