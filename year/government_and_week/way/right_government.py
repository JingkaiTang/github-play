
#! /usr/bin/env python

def little_man(str_arg):
    large_person(str_arg)
    print('great_work')

def large_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_man('be_year')
