
#! /usr/bin/env python

def child(str_arg):
    government(str_arg)
    print('make_person')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('say_man')
