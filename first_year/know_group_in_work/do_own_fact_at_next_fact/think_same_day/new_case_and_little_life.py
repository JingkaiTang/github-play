
#! /usr/bin/env python

def child_and_next_man(str_arg):
    work_new_way(str_arg)
    print('child')

def work_new_way(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child_and_next_man('try_point_under_eye')
