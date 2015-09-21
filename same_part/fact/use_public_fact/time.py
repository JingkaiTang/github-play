
#! /usr/bin/env python

def same_thing(str_arg):
    bad_case_or_last_man(str_arg)
    print('use_case')

def bad_case_or_last_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_thing('great_thing_or_early_week')
