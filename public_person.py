
#! /usr/bin/env python

def own_thing(str_arg):
    work(str_arg)
    print('good_life')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_thing('number')
