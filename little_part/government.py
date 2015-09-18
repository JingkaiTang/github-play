
#! /usr/bin/env python

def use_man_for_group(str_arg):
    woman(str_arg)
    print('high_man_or_child')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_man_for_group('big_time')
