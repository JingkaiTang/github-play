
#! /usr/bin/env python

def world(str_arg):
    part(str_arg)
    print('world')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('part')
