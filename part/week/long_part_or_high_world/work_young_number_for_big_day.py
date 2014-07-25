
#! /usr/bin/env python

def new_group(str_arg):
    life_and_part(str_arg)
    print('child')

def life_and_part(str_arg):
    print(str_arg)

if __name__ == '__main__':
    new_group('leave_company_of_few_group')
