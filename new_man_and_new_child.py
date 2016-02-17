
#! /usr/bin/env python

def same_thing(str_arg):
    give_time(str_arg)
    print('world')

def give_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_thing('able_way')
