#!/usr/bin/env python
# _*_ coding:utf-8 _*_

import sys
import requests

from ..platform import ManageProcessor


url = "http://192.168.3.32:7001/"


@ManageProcessor.plugin_register('weblogic-console')
class WeblogicCosole(object):
	def __init__(self, headers = {'user-agent': 'ceshi/0.0.1'}):
    	
    def process(self,ip,port):
        self.run(ip,port)
    def islive(self,ur,port):
        url='http://' + str(ur)+':'+str(port)+'/console/login/LoginForm.jsp'
        r = requests.get(url, headers=self.headers)
        return r.status_code

    def run(self,url,port):
        if self.islive(url,port)==200:
            u='http://' + str(url)+':'+str(port)+'/console/login/LoginForm.jsp'
			return CVE_RESULT('Weblogic后台路径存在',u)
        else:
			return None