#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 31, 2016

@author: weizhen
'''

def func():
    global x
    
    print 'x is', x
    x = 2
    print 'Change x to', x
    
x = 50
func()
print 'Value of x is', x
