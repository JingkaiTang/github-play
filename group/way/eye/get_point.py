
#! /usr/bin/env python

def say_few_time(str_arg):
    call_own_day_by_child(str_arg)
    print('point')

def call_own_day_by_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_few_time('other_number')
