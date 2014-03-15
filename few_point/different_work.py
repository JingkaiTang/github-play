
#! /usr/bin/env python

def child(str_arg):
    woman(str_arg)
    print('different_time')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('great_person')
