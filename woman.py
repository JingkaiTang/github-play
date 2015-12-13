
#! /usr/bin/env python

def call_other_work(str_arg):
    make_child(str_arg)
    print('great_government_or_company')

def make_child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_other_work('other_work')
