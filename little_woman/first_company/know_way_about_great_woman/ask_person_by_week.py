
#! /usr/bin/env python

def child(str_arg):
    large_thing(str_arg)
    print('early_life')

def large_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('person_or_number')
