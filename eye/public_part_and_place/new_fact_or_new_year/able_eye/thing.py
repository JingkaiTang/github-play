
#! /usr/bin/env python

def call_work(str_arg):
    early_case(str_arg)
    print('work_or_world')

def early_case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    call_work('good_point')
