
#! /usr/bin/env python

def have_government(str_arg):
    case(str_arg)
    print('man')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    have_government('large_point')
