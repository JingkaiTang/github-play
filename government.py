
#! /usr/bin/env python

def use_problem(str_arg):
    case_or_small_thing(str_arg)
    print('public_child')

def case_or_small_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_problem('fact')
