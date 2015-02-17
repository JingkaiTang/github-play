
#! /usr/bin/env python

def number_and_large_day(str_arg):
    number_and_year(str_arg)
    print('child')

def number_and_year(str_arg):
    print(str_arg)

if __name__ == '__main__':
    number_and_large_day('world_and_person')
