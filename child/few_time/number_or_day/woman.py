
#! /usr/bin/env python

def man_or_part(str_arg):
    place(str_arg)
    print('man')

def place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man_or_part('think_public_work')
