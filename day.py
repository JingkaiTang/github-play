
#! /usr/bin/env python

def tell_last_man(str_arg):
    public_part(str_arg)
    print('world_and_first_person')

def public_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    tell_last_man('other_year')
