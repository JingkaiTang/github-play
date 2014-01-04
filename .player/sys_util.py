#! /usr/bin/env python
import os


def cmd_wrap(*args):
    return ' '.join(args)


def str_wrap(s):
    return '"' + s + '"'


# git
def git_init():
    cmd = 'git init'
    os.system(cmd)

def git_add(files):
    cmd = cmd_wrap('git add', ' '.join(files))
    os.system(cmd)


def git_commit(msg):
    cmd = cmd_wrap('git commit -m', str_wrap(msg))
    os.system(cmd)


def git(files, msg):
    git_add(files)
    git_commit(msg)


# date
def mod_date(dt):
    cmd = cmd_wrap('sudo date -s', str_wrap(dt))
    os.system(cmd)

# mkdir
def mkdir(dir_name):
    cmd = cmd_wrap('mkdir -p', dir_name)
    
