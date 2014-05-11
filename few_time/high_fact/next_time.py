
#! /usr/bin/env python

def child(str_arg):
    thing(str_arg)
    print('eye_or_number')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('same_work_or_large_thing')
