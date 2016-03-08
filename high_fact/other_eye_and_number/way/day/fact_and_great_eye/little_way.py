
#! /usr/bin/env python

def thing(str_arg):
    part(str_arg)
    print('work_different_group')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('week')
