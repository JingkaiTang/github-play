
#! /usr/bin/env python

def eye_or_way(str_arg):
    call_work(str_arg)
    print('different_part')

def call_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye_or_way('man')
