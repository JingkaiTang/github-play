
#! /usr/bin/env python

def big_child(str_arg):
    woman(str_arg)
    print('woman')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_child('place')
