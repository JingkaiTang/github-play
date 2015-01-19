
#! /usr/bin/env python

def man(str_arg):
    give_group(str_arg)
    print('small_part')

def give_group(str_arg):
    print(str_arg)

if __name__ == '__main__':
    man('say_place_over_bad_work')
