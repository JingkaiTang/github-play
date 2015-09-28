
#! /usr/bin/env python

def eye(str_arg):
    child(str_arg)
    print('early_fact')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('first_way')
