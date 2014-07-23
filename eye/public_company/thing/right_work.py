
#! /usr/bin/env python

def child(str_arg):
    big_part(str_arg)
    print('high_way')

def big_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('work_way')
