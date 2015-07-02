
#! /usr/bin/env python

def see_government(str_arg):
    new_person_or_group(str_arg)
    print('child')

def new_person_or_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    see_government('other_day')
