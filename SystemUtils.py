#!/usr/bin/env python
# -*- coding: utf-8 -*-

from ServerInfo import ServerInfo
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
      info.local_hostname = platform.uname()[1]
      info.local_kernel = platform.local_kernel()
      info.local_os = platform.uname()[0]
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
    if command_mem == "/mem":
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

  def get_http_status(self):

    host = "www.midascoin.xyz"
    url = "https://api.telegram.org/bot574513532:AAFN3cEsV48DfFUv90wYhITiPb-nlFQ81Pg/sendMessage"
    down = "Die roi ne =))"

    conn = httplib.HTTPConnection(host)
    conn.request("HEAD", "/")
    site_status = conn.getresponse().status
    status_final = str(site_status)

    if status_final != "200":
      print status_final
      requests.post(url, data={'chat_id': 454062609, 'text': str(down)})

