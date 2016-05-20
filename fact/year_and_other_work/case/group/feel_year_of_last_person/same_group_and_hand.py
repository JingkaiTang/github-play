
#! /usr/bin/env python

def eye(str_arg):
    child(str_arg)
    print('own_company')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('way')
