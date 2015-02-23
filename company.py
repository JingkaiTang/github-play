
#! /usr/bin/env python

def eye(str_arg):
    public_group(str_arg)
    print('child')

def public_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    eye('great_work_and_year')
