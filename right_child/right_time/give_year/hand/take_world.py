
#! /usr/bin/env python

def world_and_eye(str_arg):
    take_case_with_world(str_arg)
    print('world')

def take_case_with_world(str_arg):
    print(str_arg)

if __name__ == '__main__':
    world_and_eye('able_person')
