#! /usr/bin/env python

import os
import random
import datetime
import sys
from data_parser import data_parse

MAX_FILE_DEPTH = 5
words_dict = data_parse()
rc = lambda l: lambda: random.choice(l)
rc_words = lambda key: rc(words_dict[key])
acts = rc_words('acts')
verbs = rc_words('verbs')
nouns = rc_words('nouns')
adjs = rc_words('adjs')
conjs = rc_words('conjs')
preps = rc_words('preps')
ifrand = lambda: random.choice([True, False])


def gen_code():
    return r'''
#! /usr/bin/env python

def {f0}(str_arg):
    {f1}(str_arg)
    print('{s0}')

def {f1}(str_arg):
    print(str_arg)

if __name__ == '__main__':
    {f0}('{s1}')
'''.fromat(f0=randstr(), f1=randstr(), s0=randstr(), s1=randstr())


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


def name_wrap(*args):
    return '_'.join(args)


def randnoun():
    if ifrand():
        return nouns()

    return name_wrap(adjs(), nouns())


def randstr():
    if ifrand():
        return randnoun()

    if ifrand():
        return name_wrap(randnoun(), conjs(), randnoun())

    if ifrand():
        return name_wrap(verbs(), randnoun())

    return name_wrap(verbs(), randnoun(), preps(), randnoun())


def randfile():
    depth = random.randint(0, MAX_FILE_DEPTH)
    fn = randstr() + '.py'
    for i in range(depth):
        fn = os.path.join(randstr(), fn)
    return fn


if __name__ == '__main__':
    #write2file(gen_code(), 'test.py')
    #git(['test.py'], 'mix: for test, again')
    arg_dt_from = sys.argv[1]
    arg_dt_to = sys.argv[2]
    arg_frq = sys.argv[3]
    print(randmsg(['test.py', 'hello.py']))
    print(randstr())
    print(randstr())
    print(randfile())
    print(randfile())
    print(randfile())
