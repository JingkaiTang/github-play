
#! /usr/bin/env python

def take_few_time_into_place(str_arg):
    little_child(str_arg)
    print('child')

def little_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    take_few_time_into_place('high_case')
