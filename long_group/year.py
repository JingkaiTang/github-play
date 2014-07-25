
#! /usr/bin/env python

def child(str_arg):
    great_way(str_arg)
    print('high_thing')

def great_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('few_problem')
