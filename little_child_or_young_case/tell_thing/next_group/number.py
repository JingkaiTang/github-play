
#! /usr/bin/env python

def early_thing(str_arg):
    be_other_man(str_arg)
    print('same_thing_or_early_part')

def be_other_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_thing('life_and_point')
