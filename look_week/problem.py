
#! /usr/bin/env python

def world_or_child(str_arg):
    case_and_fact(str_arg)
    print('person')

def case_and_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_or_child('fact')
