
#! /usr/bin/env python

def man(str_arg):
    early_child(str_arg)
    print('child')

def early_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('hand')
