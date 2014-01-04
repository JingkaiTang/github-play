#! /usr/bin/env python

import os
import random
import datetime
import sys
from data_parser import data_parse



words_dict = data_parse()
rc = lambda l: lambda: random.choice(l)
rc_words = lambda key: rc(words_dict[key])
acts = rc_words('acts')
verbs = rc_words('verbs')
nouns = rc_words('nouns')
adjs = rc_words('adjs')
conjs = rc_words('conjs')
preps = rc_words('preps')


def gen_code():
    return r'''
#! /usr/bin/env python
if __name__ == '__main__':
    print("hello")
'''


def write2file(raw_code, file_name):
    open(file_name, 'w').write(raw_code)


def randmsg(files):
    f_msg = ''
    if len(files) > 1:
        f_msg = ', '.join(files[:-1]) + ' ' + conjs() + ' ' + files[-1]
    else:
        f_msg = ' '.join(files)
    return '{act}: {verb} {f_msg} {prep} {adj} {noun}'.format(
        act=acts(),
        verb=verbs(),
        f_msg=f_msg,
        prep=preps(),
        adj=adjs(),
        noun=nouns()
    )


if __name__ == '__main__':
    #write2file(gen_code(), 'test.py')
    #git(['test.py'], 'mix: for test, again')
    arg_dt_from = sys.args[1]
    arg_dt_to = sys.args[2]
    arg_frq = sys.args[3]
    print(randmsg(['test.py', 'hello.py']))
