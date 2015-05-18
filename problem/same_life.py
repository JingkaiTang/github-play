
#! /usr/bin/env python

def man(str_arg):
    look_part(str_arg)
    print('eye_or_man')

def look_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('world')
