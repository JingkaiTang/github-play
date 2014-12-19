
#! /usr/bin/env python

def get_person_over_man(str_arg):
    take_child(str_arg)
    print('man')

def take_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    get_person_over_man('other_man')
