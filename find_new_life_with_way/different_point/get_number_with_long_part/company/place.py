
#! /usr/bin/env python

def say_case(str_arg):
    thing(str_arg)
    print('call_hand')

def thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    say_case('try_public_work')
