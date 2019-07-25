#!/usr/bin/env python
# _*_ coding:utf-8 _*_


class CVE(object):
    def __init__(self, headers={'user-agent': 'ceshi/0.0.1'}):
        self.headers = headers

    def process(self,ip,port):
        self.run(ip,port)

    def islive(self,ur,port):
        return 500

    def run(self,url,port):
        return None

class CVE_RESULT(object):
    def __init__(cve,url='/'):
        self.cve = cve
        sefl.url = url
