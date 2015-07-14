
#! /usr/bin/env python

def make_child(str_arg):
    say_thing_above_place(str_arg)
    print('think_right_fact')

def say_thing_above_place(str_arg):
    print(str_arg)

if __name__ == '__main__':
    make_child('hand_or_small_person')
