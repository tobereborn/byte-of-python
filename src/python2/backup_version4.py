#!/usr/bin/python
# -*- coding:utf-8 -*-

'''
Created on Jan 1, 2017

@author: weizhen
'''

import os
import time

source = ['/home/weizhen/TbrGitHub/tmp/t1', '/home/weizhen/TbrGitHub/tmp/f3']
target_dir = '/home/weizhen/TbrGitHub/tmp/backup'

today = target_dir + time.strftime('%Y%m%d')
now = time.strftime('%H%M%s')

comment = raw_input('Enter a comment:')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'
    

if not os.path.exists(today):
    os.mkdir(today)
    print 'Successfully created directory', today


zip_command = "zip -qr '%s' %s" % (target, ' '.join(source))

print zip_command

if os.system(zip_command) == 0:
    print 'Successful backup to', target
else:
    print 'Backup FAILED'