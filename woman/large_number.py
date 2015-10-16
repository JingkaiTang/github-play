
#! /usr/bin/env python

def little_thing_and_other_child(str_arg):
    man(str_arg)
    print('old_case')

def man(str_arg):
    print(str_arg)

if __name__ == '__main__':
    little_thing_and_other_child('ask_fact_on_number')
