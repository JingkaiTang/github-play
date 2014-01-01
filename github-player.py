#! /usr/bin/env python

import os

def cmd_wrap(*args):
    return ' '.join(args)

def str_wrap(s):
    return '"' + s + '"'

def gen_code():
    return r'''
#! /usr/bin/env python
if __name__ == '__main__':
    print("hello")
'''

def write2file(raw_code, file_name):
    open(file_name, 'w').write(raw_code)

def git_add(files):
    cmd = cmd_wrap('git add', ' '.join(files))
    os.system(cmd)

def git_commit(msg):
    cmd = cmd_wrap('git commit -m', str_wrap(msg))
    os.system(cmd)

def git(files, msg):
    git_add(files)
    git_commit(msg)

if __name__ == '__main__':
    write2file(gen_code(), 'test.py')
    git(['test.py'], 'mix: for test, again')
    

