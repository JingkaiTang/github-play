
#! /usr/bin/env python

def make_fact(str_arg):
    next_number_or_case(str_arg)
    print('call_last_case')

def next_number_or_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_fact('thing_and_own_woman')
