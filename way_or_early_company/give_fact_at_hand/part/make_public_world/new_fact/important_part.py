
#! /usr/bin/env python

def other_man(str_arg):
    see_child(str_arg)
    print('other_day_and_problem')

def see_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_man('thing')
