
#! /usr/bin/env python

def first_point(str_arg):
    first_person(str_arg)
    print('other_point')

def first_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    first_point('young_eye')
