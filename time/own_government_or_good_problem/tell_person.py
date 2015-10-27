
#! /usr/bin/env python

def go_work(str_arg):
    work(str_arg)
    print('bad_person')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_work('look_work')
