
#! /usr/bin/env python

def thing(str_arg):
    make_thing_for_other_person(str_arg)
    print('able_place')

def make_thing_for_other_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('next_world')
