# -*- coding: UTF-8 -*- 
# サンプリングテスト用 dig

import subprocess
import codecs

file = codecs.open('fqdn_list', 'r', encoding='UTF-8')
dig_list = file.readlines()

for i in dig_list:
    print (i.strip(), end=' --> ')
    print (subprocess.check_output(['dig', '+short', i.strip()],universal_newlines=True),end='')