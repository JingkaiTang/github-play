
#! /usr/bin/env python

def work_and_child(str_arg):
    eye(str_arg)
    print('time')

def eye(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_and_child('old_life')
