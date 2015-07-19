
#! /usr/bin/env python

def woman(str_arg):
    public_woman(str_arg)
    print('get_group')

def public_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    woman('tell_point')
