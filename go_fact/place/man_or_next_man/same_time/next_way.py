
#! /usr/bin/env python

def thing(str_arg):
    big_thing(str_arg)
    print('new_day')

def big_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('number_and_new_way')
