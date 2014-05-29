
#! /usr/bin/env python

def use_fact_above_public_man(str_arg):
    call_fact(str_arg)
    print('own_child')

def call_fact(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_fact_above_public_man('great_number_or_eye')
