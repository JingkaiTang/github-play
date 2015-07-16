
#! /usr/bin/env python

def other_child(str_arg):
    own_place(str_arg)
    print('find_same_child_after_fact')

def own_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_child('young_number')
