
#! /usr/bin/env python

def bad_thing(str_arg):
    part(str_arg)
    print('hand')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_thing('feel_part')
