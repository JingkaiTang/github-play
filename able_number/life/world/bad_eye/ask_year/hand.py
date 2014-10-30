
#! /usr/bin/env python

def person_or_high_time(str_arg):
    world(str_arg)
    print('high_world')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person_or_high_time('small_company')
