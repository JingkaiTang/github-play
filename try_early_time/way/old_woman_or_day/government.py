
#! /usr/bin/env python

def person(str_arg):
    child(str_arg)
    print('point')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('own_number_and_same_part')
