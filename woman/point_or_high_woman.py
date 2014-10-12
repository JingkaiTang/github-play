
#! /usr/bin/env python

def public_person(str_arg):
    world(str_arg)
    print('way')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_person('different_point')
