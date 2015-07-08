
#! /usr/bin/env python

def try_own_man(str_arg):
    man_or_child(str_arg)
    print('come_early_part')

def man_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    try_own_man('come_other_place_for_same_week')
