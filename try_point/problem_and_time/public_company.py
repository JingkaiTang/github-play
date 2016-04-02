
#! /usr/bin/env python

def young_man(str_arg):
    woman(str_arg)
    print('call_own_man')

def woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    young_man('get_big_number_about_next_part')
