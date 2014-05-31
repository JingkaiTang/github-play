
#! /usr/bin/env python

def thing(str_arg):
    own_place(str_arg)
    print('good_way_or_number')

def own_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing('part')
