
#! /usr/bin/env python

def early_work_or_first_place(str_arg):
    fact(str_arg)
    print('child')

def fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_work_or_first_place('part')
