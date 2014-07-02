
#! /usr/bin/env python

def same_number(str_arg):
    part(str_arg)
    print('child')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_number('same_child')
