#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

class ShortInputException(Exception):
    '''A user-defined exception class.'''
    def __init__(self, length, atleast):
        self.length = length
        self.atleast = atleast
    
try:
    s = raw_input('Enter something -->')
    if len(s) < 3:
        raise ShortInputException(len(s), 3)
        
except EOFError:
    print '\nWhy did you do an EOF on me>'
except ShortInputException, x:
    print '\nThe input was of lenght %d,it should be at least %d'\
    % (x.length, x.atleast)
else:
    print 'No exception was raised.'