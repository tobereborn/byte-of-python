#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

import cPickle

shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']

f = file(shoplistfile, 'w')
cPickle.dump(shoplist, f)
f.close()

del shoplist

f = file(shoplistfile)
storedlist = cPickle.load(f)
print storedlist
