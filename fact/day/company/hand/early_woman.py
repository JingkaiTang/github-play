
#! /usr/bin/env python

def own_world(str_arg):
    go_number_by_fact(str_arg)
    print('other_way')

def go_number_by_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    own_world('case')
