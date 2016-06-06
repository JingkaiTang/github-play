
#! /usr/bin/env python

def public_case(str_arg):
    big_case_or_other_thing(str_arg)
    print('old_world')

def big_case_or_other_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_case('large_government')
