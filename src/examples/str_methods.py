#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

name = 'Swaroop'  # This is a string object

if name.startswith('Swa'):
    print 'Yes,the string starts with "Swa"'

if 'a' in name:
    print 'Yes,it contains the string "a"'

if name.find('war') != -1:
    print 'Yes,it contains the string "war"'

delimiter = '_*_'
mylist = ['India', 'China', 'Finaland', 'Brazil']
print delimiter.join(mylist)