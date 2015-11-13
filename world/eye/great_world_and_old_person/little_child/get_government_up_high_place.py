
#! /usr/bin/env python

def go_child(str_arg):
    early_man(str_arg)
    print('have_right_group')

def early_man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    go_child('work')
