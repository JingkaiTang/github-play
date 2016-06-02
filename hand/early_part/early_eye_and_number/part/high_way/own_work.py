
#! /usr/bin/env python

def point(str_arg):
    own_thing(str_arg)
    print('work')

def own_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('go_part')
