
#! /usr/bin/env python

def big_child(str_arg):
    long_way(str_arg)
    print('life_and_group')

def long_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_child('long_person')
