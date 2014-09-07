
#! /usr/bin/env python

def child_and_way(str_arg):
    big_way(str_arg)
    print('way')

def big_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_way('seem_case')
