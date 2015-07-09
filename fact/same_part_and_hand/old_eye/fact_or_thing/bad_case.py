
#! /usr/bin/env python

def big_woman_and_group(str_arg):
    woman(str_arg)
    print('little_problem')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_woman_and_group('man')
