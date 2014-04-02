
#! /usr/bin/env python

def thing_or_eye(str_arg):
    child(str_arg)
    print('new_thing')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_or_eye('life')
