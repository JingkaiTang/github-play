
#! /usr/bin/env python

def world(str_arg):
    work(str_arg)
    print('call_new_work_after_person')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world('way')
