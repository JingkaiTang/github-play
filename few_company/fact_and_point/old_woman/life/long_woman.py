
#! /usr/bin/env python

def child_or_world(str_arg):
    way(str_arg)
    print('little_problem')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_world('small_number')
