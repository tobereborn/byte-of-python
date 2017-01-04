#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

try:
    f = file('poem.txt')
    while True:
        l = f.readline()
        if len(l) == 0:
            break
        print l,
finally:
    print 'Cleaning up...'
    f.close()
