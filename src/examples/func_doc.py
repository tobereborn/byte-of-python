#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 31, 2016

@author: weizhen
'''

def printMax(x, y):
    '''Prints the maximum of the two numbers
       
       The two values must be integers. If not,
       they are converted to integers.'''
    
    x = int(x)
    y = int(y)
    
    if x > y:
        print x, 'is maximum'
    else:
        print y, 'is maximum'

printMax(3, 5)
print printMax.__doc__
