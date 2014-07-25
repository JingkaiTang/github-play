
#! /usr/bin/env python

def big_way(str_arg):
    old_work(str_arg)
    print('life')

def old_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    big_way('world')
