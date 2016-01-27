
#! /usr/bin/env python

def good_person(str_arg):
    life_and_large_case(str_arg)
    print('call_other_way')

def life_and_large_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    good_person('right_place_or_few_child')
