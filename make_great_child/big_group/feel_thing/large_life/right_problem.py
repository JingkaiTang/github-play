
#! /usr/bin/env python

def fact(str_arg):
    public_part(str_arg)
    print('little_number')

def public_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    fact('big_way')
