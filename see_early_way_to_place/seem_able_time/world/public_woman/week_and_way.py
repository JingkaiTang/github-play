
#! /usr/bin/env python

def child(str_arg):
    make_way(str_arg)
    print('great_part')

def make_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('last_person')
