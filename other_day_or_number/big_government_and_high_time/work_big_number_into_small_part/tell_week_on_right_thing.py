
#! /usr/bin/env python

def old_way(str_arg):
    give_person(str_arg)
    print('long_person')

def give_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    old_way('different_person')
