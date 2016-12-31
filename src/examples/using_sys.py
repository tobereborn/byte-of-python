#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 31, 2016

@author: weizhen
'''

import sys

print 'The command line arguments used are.'
for i in sys.argv:
    print i

print '\n\nThe PYTHONPATH is', sys.path, '\n'
