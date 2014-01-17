
#! /usr/bin/env python

def give_long_work(str_arg):
    great_part(str_arg)
    print('child')

def great_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    give_long_work('little_way')
