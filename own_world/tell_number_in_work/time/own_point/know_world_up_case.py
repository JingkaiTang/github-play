
#! /usr/bin/env python

def thing(str_arg):
    hand_and_group(str_arg)
    print('public_point')

def hand_and_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('call_fact_up_little_way')
