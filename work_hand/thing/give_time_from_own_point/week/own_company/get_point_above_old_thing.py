
#! /usr/bin/env python

def see_world(str_arg):
    part(str_arg)
    print('other_way')

def part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_world('see_old_government_after_same_day')
