
#! /usr/bin/env python

def other_person(str_arg):
    company(str_arg)
    print('way')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_person('world')
