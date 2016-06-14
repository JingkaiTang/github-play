
#! /usr/bin/env python

def work(str_arg):
    thing_or_time(str_arg)
    print('good_part')

def thing_or_time(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work('bad_company_and_time')
