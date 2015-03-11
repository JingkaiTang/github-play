
#! /usr/bin/env python

def child_or_child(str_arg):
    work(str_arg)
    print('first_work')

def work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_or_child('part')
