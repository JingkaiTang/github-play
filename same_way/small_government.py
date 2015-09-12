
#! /usr/bin/env python

def other_week(str_arg):
    other_group(str_arg)
    print('old_group')

def other_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    other_week('way')
