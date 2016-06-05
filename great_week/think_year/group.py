
#! /usr/bin/env python

def use_few_child_beneath_different_fact(str_arg):
    child(str_arg)
    print('young_child')

def child(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_few_child_beneath_different_fact('old_life')
