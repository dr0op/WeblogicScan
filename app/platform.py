#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class ManageProcessor(object):
    PLUGINS = {}

    def process(self,ip,port,plugins=()):
        if plugins is ():
            for plugin_name in self.PLUGINS.keys():
                try:
                    print(Color.OKYELLOW+"[*]开始检测",plugin_name+Color.ENDC)
                    self.PLUGINS[plugin_name]().process(ip,port)
                except:
                    print (Color.WARNING+"[-]{} 未成功检测，请检查网络连接或或目标存在负载中间件".format(plugin_name)+Color.ENDC)
        else:
            for plugin_name in plugins:
                try:
                    print("[*]开始检测 ",self.PLUGINS[plugin_name])
                    self.PLUGINS[plugin_name]().process(ip,port)
                except:
                    print ("[-]{}未成功检测，请检查网络连接或或目标存在负载中间".format(self.PLUGINS[plugin_name]))
        return

    @classmethod
    def plugin_register(cls, plugin_name):
        def wrapper(plugin):
            cls.PLUGINS.update({plugin_name:plugin})
            return plugin
        return wrapper

class Color:
    HEADER = '\033[95m'
    OKBLUE = '\033[90m'
    OKGREEN = '\033[92m'
    OKYELLOW = '\33[93m'
    WARNING = '\033[91m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'



