
#! /usr/bin/env python

def same_work(str_arg):
    early_work(str_arg)
    print('man')

def early_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_work('last_company_or_new_year')
