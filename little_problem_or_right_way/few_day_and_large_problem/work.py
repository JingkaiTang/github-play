
#! /usr/bin/env python

def great_work(str_arg):
    public_hand(str_arg)
    print('little_problem')

def public_hand(str_arg):
    print(str_arg)

if __name__ == '__main__':
    great_work('good_person')
