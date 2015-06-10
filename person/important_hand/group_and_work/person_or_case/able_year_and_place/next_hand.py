
#! /usr/bin/env python

def person(str_arg):
    public_person(str_arg)
    print('own_time_and_last_hand')

def public_person(str_arg):
    print(str_arg)

if __name__ == '__main__':
    person('same_week')
