
#! /usr/bin/env python

def child(str_arg):
    man_and_few_world(str_arg)
    print('few_way')

def man_and_few_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('little_child')
