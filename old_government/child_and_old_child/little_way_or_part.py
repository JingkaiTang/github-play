
#! /usr/bin/env python

def company_or_case(str_arg):
    own_company(str_arg)
    print('thing')

def own_company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    company_or_case('person')
