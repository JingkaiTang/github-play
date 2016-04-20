
#! /usr/bin/env python

def different_work(str_arg):
    way(str_arg)
    print('work')

def way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_work('other_group_and_important_child')
