
#! /usr/bin/env python

def world(str_arg):
    use_part(str_arg)
    print('bad_world')

def use_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('company')
