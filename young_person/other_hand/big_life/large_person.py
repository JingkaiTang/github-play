
#! /usr/bin/env python

def do_other_way_beneath_problem(str_arg):
    case(str_arg)
    print('important_group')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_other_way_beneath_problem('child')
