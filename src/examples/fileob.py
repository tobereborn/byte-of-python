#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

poem = '''\
Programming is fun
When the work is done
if (you wanna make your work also fun):
use Python!
'''

f = file('poem.txt', 'w')
f.write(poem)
f.close()

f = file('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:  # EOF
        break
    print line,  # So that extra newline is not added
f.close()
#
