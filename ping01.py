# -*- coding: utf-8 -*- 
# ping

'''
Usage: $python ping01.py ip_list
'''

import subprocess

file = open('ip_list', 'r')
ping_list = file.readlines()

for i in ping_list:
    result = subprocess.call(['fping', i.strip()], universal_newlines=True)
    
    if result == 0:
        print ()
    else:
        print ("!!!!!unreacheable!!!!!", '\n')