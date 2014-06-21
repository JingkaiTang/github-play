
#! /usr/bin/env python

def new_company(str_arg):
    important_child(str_arg)
    print('group')

def important_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_company('part')
