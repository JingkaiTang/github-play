
#! /usr/bin/env python

def thing_or_other_child(str_arg):
    big_group_or_child(str_arg)
    print('come_few_child_with_small_life')

def big_group_or_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_or_other_child('life')
