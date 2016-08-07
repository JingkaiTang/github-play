
#! /usr/bin/env python

def different_child(str_arg):
    case(str_arg)
    print('work')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    different_child('important_thing_and_way')
