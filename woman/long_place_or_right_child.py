
#! /usr/bin/env python

def want_first_case(str_arg):
    case(str_arg)
    print('case_and_large_work')

def case(str_arg):
    print(str_arg)

if __name__ == '__main__':
    want_first_case('tell_big_person')
