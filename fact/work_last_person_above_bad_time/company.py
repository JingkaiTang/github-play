
#! /usr/bin/env python

def use_great_hand_in_same_case(str_arg):
    bad_point(str_arg)
    print('old_hand')

def bad_point(str_arg):
    print(str_arg)

if __name__ == '__main__':
    use_great_hand_in_same_case('own_year_or_child')
