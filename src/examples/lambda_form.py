#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

def make_repeater(n):
    return lambda s:s * n

twice = make_repeater(2)
twicetheword = twice('word')
print twicetheword
