
#! /usr/bin/env python

def do_world_on_man(str_arg):
    child(str_arg)
    print('big_day')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    do_world_on_man('person_and_way')
