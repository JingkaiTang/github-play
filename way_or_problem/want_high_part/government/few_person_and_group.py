
#! /usr/bin/env python

def eye_or_work(str_arg):
    world(str_arg)
    print('work_same_person')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_or_work('little_child')
