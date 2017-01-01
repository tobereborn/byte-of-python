#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

import sys

def readfile(filename):
    '''Print a file to the stdout.'''
    f = file(filename)
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print line,
    f.close()

### Main ####
if len(sys.argv) < 2:
    print 'No action specified.'
    sys.exit()
    
if sys.argv[1].startwith('--'):
    option = sys.argv[1][2:]
    # Fetch sys.argv[1] and copy the string except for first two characters
    if option == 'version':
        print 'Version 1.00'
    elif option == 'help':
        print '''\
This program prints files to the standard output.
Any number of files can be specified.
Options include:
--version : Prints the version number and exits
--help : Prints this help and exits'''
    else:
        print 'Unknown option.'
else:
    for filename in sys.argv[1:]:
        readfile(filename)