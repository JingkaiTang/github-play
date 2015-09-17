
#! /usr/bin/env python

def early_child(str_arg):
    early_fact(str_arg)
    print('child')

def early_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    early_child('few_life')
