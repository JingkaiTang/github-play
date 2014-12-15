
#! /usr/bin/env python

def same_work(str_arg):
    woman(str_arg)
    print('day_or_woman')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_work('person_and_fact')
