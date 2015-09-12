
#! /usr/bin/env python

def hand(str_arg):
    great_part_and_early_part(str_arg)
    print('child')

def great_part_and_early_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    hand('life')
