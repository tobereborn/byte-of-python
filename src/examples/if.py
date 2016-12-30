#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 30, 2016

@author: weizhenjin
'''

number = 25
guess = int(raw_input('Enter an integer:'))

if guess == number:
    print 'You got it.'
elif guess < number:
    print 'No, it is a little higher than that.'
else:
    print 'No, it is a little lower than that.'
print 'Done'
