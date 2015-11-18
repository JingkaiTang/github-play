
#! /usr/bin/env python

def little_day(str_arg):
    thing(str_arg)
    print('child')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_day('great_person_and_good_man')
