
#! /usr/bin/env python

def public_child(str_arg):
    point_or_bad_person(str_arg)
    print('thing')

def point_or_bad_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_child('different_woman')
