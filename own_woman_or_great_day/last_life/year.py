
#! /usr/bin/env python

def early_week(str_arg):
    work(str_arg)
    print('child')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_week('say_right_year')
