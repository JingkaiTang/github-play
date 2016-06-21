
#! /usr/bin/env python

def public_hand_or_work(str_arg):
    government(str_arg)
    print('take_government')

def government(str_arg):
    print(str_arg)

if __name__ == '__main__':
    public_hand_or_work('be_way')
