
#! /usr/bin/env python

def see_different_child(str_arg):
    public_man(str_arg)
    print('way')

def public_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_different_child('early_year_and_important_thing')
