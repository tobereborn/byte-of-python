#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Dec 31, 2016

@author: weizhen
'''

ab = {'Swaroop':'python@g2swaroop.net',
      'Miguel' : 'miguel@novell.com',
      'Larry' : 'larry@wall.org',
      'Spammer' : 'spammer@hotmail.com'
    }

print "Swaroop's address is %s" % ab['Swaroop']

ab['Guido'] = 'guido@python.org'
del ab['Spammer']

print '\nThere are %d contacts in the address-book\n' % len(ab)

for name, address in ab.items():
    print 'Contact %s at %s' % (name, address)
    
if ab.has_key('Guido'):
    print "\nGuido's address is %s" % ab['Guido']
