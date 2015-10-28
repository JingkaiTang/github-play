
#! /usr/bin/env python

def person(str_arg):
    go_child(str_arg)
    print('say_old_eye')

def go_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('number')
