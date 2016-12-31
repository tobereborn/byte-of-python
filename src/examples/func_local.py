#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 31, 2016

@author: weizhen
'''

def func(x):
    print 'Local x is', x
    x = 2
    print 'Change local x to', x

x = 50
func(x)
print 'x is still', x
