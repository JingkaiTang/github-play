
#! /usr/bin/env python

def work_child(str_arg):
    place(str_arg)
    print('first_point')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_child('fact')
