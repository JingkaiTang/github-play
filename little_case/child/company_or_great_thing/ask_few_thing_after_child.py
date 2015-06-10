
#! /usr/bin/env python

def big_child(str_arg):
    point(str_arg)
    print('old_way_and_other_child')

def point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_child('find_fact')
