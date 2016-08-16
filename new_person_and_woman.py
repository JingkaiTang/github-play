
#! /usr/bin/env python

def try_same_government(str_arg):
    person(str_arg)
    print('person')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_same_government('other_time')
