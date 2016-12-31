#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

shoplist = ['apple', 'mango', 'carrot', 'banana']
mylist = shoplist
# mylist is just another reference to the same list

del shoplist[0]
# I purchased the first item, so i remove it from the lsit.

print 'shoplist is', shoplist
print 'mylist is', mylist
# Notice that shoplist and mylist both print a list without the
# 'apple' confirming that they refer to the same list object

mylist = shoplist[:]
# @Obtain a full slice to make a copy
del mylist[0]

print 'shoplist is', shoplist
print 'mylist is', mylist
# Notice now that the two lists are different