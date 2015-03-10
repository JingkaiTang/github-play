
#! /usr/bin/env python

def woman(str_arg):
    man(str_arg)
    print('get_person')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('find_important_part_from_number')
