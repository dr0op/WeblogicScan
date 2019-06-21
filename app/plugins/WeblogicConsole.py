#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import logging
import sys
import requests

from ..platform import ManageProcessor,Color

logging.basicConfig(filename='Weblogic.log',
                        format='%(asctime)s %(message)s',
                        filemode="w", level=logging.INFO)

url = "http://192.168.3.32:7001/"


@ManageProcessor.plugin_register('weblogic-console')
class WeblogicCosole(object):
    headers = {'user-agent': 'ceshi/0.0.1'}
    def process(self,ip,port):
        self.run(ip,port)
    def islive(self,ur,port):
        url='http://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
        r = requests.get(url, headers=self.headers)
        return r.status_code

    def run(self,url,port):
        if self.islive(url,port)==200:
            u='http://' + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
            logging.info("[+]The target Weblogic console address is exposed! The path is: {} Please try weak password blasting!".format(u))
            print(Color.OKBLUE+"[+]The target Weblogic console address is exposed!\n[+]The path is: {}\n[+]Please try weak password blasting!".format(u)+Color.ENDC)
            print(Color.OKGREEN+'[+]Weblogic后台路径存在'+Color.ENDC)
        else:
            logging.info('[-]Target Weblogic console address not found!')
            print(Color.FAIL+"[-]Target Weblogic console address not found!"+Color.ENDC)
