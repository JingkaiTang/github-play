
#! /usr/bin/env python

def thing(str_arg):
    call_public_work(str_arg)
    print('good_government')

def call_public_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('public_group')
