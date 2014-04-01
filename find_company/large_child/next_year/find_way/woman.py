
#! /usr/bin/env python

def give_different_group(str_arg):
    man(str_arg)
    print('world_or_group')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    give_different_group('child')
