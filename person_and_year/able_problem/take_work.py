
#! /usr/bin/env python

def person(str_arg):
    public_person(str_arg)
    print('right_part')

def public_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('time')
