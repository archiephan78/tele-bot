#!/usr/bin/env python
# -*- coding: utf-8 -*-

from serverinfo import ServerInfo
import os
import platform
import httplib
import requests

class SystemUtils(object):

    def get_info_server(self, command_info):
        if command_info == "/info":
            info = ServerInfo()
            info.local_distributive = platform.linux_distribution()
            info.local_architecture = platform.architecture()
            info.local_hostname = platform.uname()[0]
            info.local_kernel = platform.release()
            info.local_os = platform.uname()[1]
        else:
            print "Cant get info"
        return info

    def get_load_server(self, command_load):
        if command_load == "/load":
            load_avg = os.getloadavg()
            load_avg = "Current Load: " + str(load_avg)
        else:
            print "Cant get info"
        return load_avg

    def get_mem_server(self, command_mem):
        if command_mem == "/memory":
            with open('/proc/meminfo', 'r') as mem:
                ret = {}
                tmp = 0
                for i in mem:
                    sline = i.split()
                    if str(sline[0]) == 'MemTotal:':
                        ret['total'] = int(sline[1])
                    elif str(sline[0]) in ('MemFree:', 'Buffers:', 'Cached:'):
                        tmp += int(sline[1])
                ret['free'] = tmp
                ret['used'] = int(ret['total']) - int(ret['free'])
                mem = "Memory info: " + str(ret)
        else:
            print "Cant get data"
        return mem
