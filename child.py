
#! /usr/bin/env python

def use_child_up_different_child(str_arg):
    case_and_important_number(str_arg)
    print('man')

def case_and_important_number(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_child_up_different_child('public_year')
