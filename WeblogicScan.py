#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys

from app.main import pentest
from app.platform import Color

version = "1.3.1"
banner='''
__        __   _     _             _        ____                  
\ \      / /__| |__ | | ___   __ _(_) ___  / ___|  ___ __ _ _ __  
 \ \ /\ / / _ \ '_ \| |/ _ \ / _` | |/ __| \___ \ / __/ _` | '_ \ 
  \ V  V /  __/ |_) | | (_) | (_| | | (__   ___) | (_| (_| | | | |
   \_/\_/ \___|_.__/|_|\___/ \__, |_|\___| |____/ \___\__,_|_| |_|
                             |___/ 
      From WeblogicScan V1.2 Fixed by Ra1ndr0op: drops.org.cn | V {} 
'''.format(version)
print(Color.OKYELLOW+banner+Color.ENDC)
print('Welcome To WeblogicScan !!')
if len(sys.argv)<3:
    print('Usage: python3 WeblogicScan [IP] [PORT]')
else:
    ip = sys.argv[1]
    port = int(sys.argv[2])
    pentest(ip,port)

