
#! /usr/bin/env python

def give_time(str_arg):
    thing_and_number(str_arg)
    print('important_number')

def thing_and_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    give_time('last_man')
