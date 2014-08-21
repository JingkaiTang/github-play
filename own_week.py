
#! /usr/bin/env python

def child(str_arg):
    other_fact(str_arg)
    print('way')

def other_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('group')
