#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 30, 2016

@author: weizhenjin
'''

while True:
    s = raw_input('Enter something:')
    if s == 'quit':
        break
    if len(s) < 3:
        continue
    print 'Sufficient length'
