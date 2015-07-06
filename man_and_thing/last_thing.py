
#! /usr/bin/env python

def thing_and_big_eye(str_arg):
    public_thing(str_arg)
    print('place')

def public_thing(str_arg):
    print(str_arg)

if __name__ == '__main__':
    thing_and_big_eye('call_old_part')
