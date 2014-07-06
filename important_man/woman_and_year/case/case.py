
#! /usr/bin/env python

def work_child(str_arg):
    young_woman(str_arg)
    print('other_part')

def young_woman(str_arg):
    print(str_arg)

if __name__ == '__main__':
    work_child('call_life')
