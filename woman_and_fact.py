
#! /usr/bin/env python

def case(str_arg):
    big_work(str_arg)
    print('work')

def big_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    case('small_person')
