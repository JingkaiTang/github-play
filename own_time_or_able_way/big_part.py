
#! /usr/bin/env python

def child(str_arg):
    little_woman(str_arg)
    print('have_other_way')

def little_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    child('have_man_by_woman')
