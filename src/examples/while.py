#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 30, 2016

@author: weizhenjin
'''

number = 23
stop = False

while not stop:
    guess = int(raw_input('Enter an integer:'))
    
    if guess == number:
        print 'You got it.'
        stop = True
    elif guess < number:
        print 'No,it is a little higher than that.'
    else:
        print 'No,it is a little lower than that.'
# else:
#     print 'The loop is over.'

print 'Done'
