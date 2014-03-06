
#! /usr/bin/env python

def be_child(str_arg):
    company(str_arg)
    print('child_and_last_company')

def company(str_arg):
    print(str_arg)

if __name__ == '__main__':
    be_child('young_hand')
