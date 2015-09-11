
#! /usr/bin/env python

def thing(str_arg):
    next_person(str_arg)
    print('bad_way')

def next_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('be_public_case_of_public_person')
