
#! /usr/bin/env python

def child(str_arg):
    person(str_arg)
    print('work')

def person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('part_or_good_thing')
