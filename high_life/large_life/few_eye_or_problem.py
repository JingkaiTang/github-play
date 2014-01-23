
#! /usr/bin/env python

def point(str_arg):
    do_part(str_arg)
    print('other_part_and_different_hand')

def do_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    point('thing_or_high_part')
