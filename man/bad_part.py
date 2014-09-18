
#! /usr/bin/env python

def life_or_case(str_arg):
    give_world(str_arg)
    print('child')

def give_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    life_or_case('able_case_or_large_way')
