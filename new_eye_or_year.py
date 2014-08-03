
#! /usr/bin/env python

def early_thing(str_arg):
    early_part(str_arg)
    print('hand')

def early_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_thing('man_or_life')
