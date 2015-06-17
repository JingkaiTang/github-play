
#! /usr/bin/env python

def work_good_case(str_arg):
    life(str_arg)
    print('call_good_child')

def life(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_good_case('go_woman')
