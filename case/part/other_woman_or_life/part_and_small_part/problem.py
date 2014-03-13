
#! /usr/bin/env python

def leave_fact(str_arg):
    part(str_arg)
    print('call_place')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    leave_fact('thing_or_place')
