
#! /usr/bin/env python

def man(str_arg):
    woman(str_arg)
    print('good_point_and_man')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('world')
