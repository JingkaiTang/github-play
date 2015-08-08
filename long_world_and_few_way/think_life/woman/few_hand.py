
#! /usr/bin/env python

def bad_place(str_arg):
    hand(str_arg)
    print('way')

def hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    bad_place('world_and_work')
