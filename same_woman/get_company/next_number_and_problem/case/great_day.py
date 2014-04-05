
#! /usr/bin/env python

def say_work(str_arg):
    child(str_arg)
    print('world')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_work('new_week')
