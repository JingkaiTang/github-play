
#! /usr/bin/env python

def eye(str_arg):
    do_work(str_arg)
    print('thing')

def do_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('work')
