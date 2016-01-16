
#! /usr/bin/env python

def place(str_arg):
    call_government_after_child(str_arg)
    print('next_place')

def call_government_after_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    place('woman')
