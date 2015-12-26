
#! /usr/bin/env python

def work(str_arg):
    world(str_arg)
    print('come_child')

def world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('work_way')
