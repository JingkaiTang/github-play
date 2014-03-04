
#! /usr/bin/env python

def little_problem(str_arg):
    child(str_arg)
    print('little_place_or_work')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_problem('time')
