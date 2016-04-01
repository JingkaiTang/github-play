
#! /usr/bin/env python

def new_number_or_group(str_arg):
    small_world(str_arg)
    print('own_part_or_way')

def small_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_number_or_group('different_case')
