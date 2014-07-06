
#! /usr/bin/env python

def same_work(str_arg):
    different_work(str_arg)
    print('little_eye')

def different_work(str_arg):
    print(str_arg)

if __name__ == '__main__':
    same_work('new_person_or_early_woman')
