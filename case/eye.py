
#! /usr/bin/env python

def go_man(str_arg):
    try_point_by_place(str_arg)
    print('child')

def try_point_by_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_man('way')
