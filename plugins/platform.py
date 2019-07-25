#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class ManageProcessor(object):
    PLUGINS = {}

    def process(self,ip,port,plugins=()):
        if plugins is ():
            for plugin_name in self.PLUGINS.keys():
                try:
                    cve = self.PLUGINS[plugin_name]().process(ip,port)
                    if cve:
                        return cve
                except:
                    return None
        else:
            for plugin_name in plugins:
                try:
                    cve = self.PLUGINS[plugin_name]().process(ip,port)
                    if cve:
                        return cve
                except:
                    return None
        return

    @classmethod
    def plugin_register(cls, plugin_name):
        def wrapper(plugin):
            cls.PLUGINS.update({plugin_name:plugin})
            return plugin
        return wrapper



