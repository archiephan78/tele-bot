#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import urllib
import json
import requests
from SystemUtils import SystemUtils
import os
import time
import threading

class BotApi(object):

  def __init__(self):
    self.json_reponse = None

  bot_api = 'https://api.telegram.org/bot574513532:AAFN3cEsV48DfFUv90wYhITiPb-nlFQ81Pg'
  status_json = '/getUpdates'
  send_message_method = '/sendMessage'
  update_url = bot_api + status_json
  group_id = 454062609

  load_command = "/load"
  info_command = "/info"
  help_command = "/help"
  mem_command = "/memory"
  check_site_status = "/check_site_status"

  def send_message(self, command, infomation):
    help_message = "You asked for /help"
    error_message = "Wrong command!"

    if command == BotApi.load_command:
      http_post = requests.post(BotApi.bot_api + self.send_message_method, data={'chatid': 454062609, 'text': str(infomation)})
      print "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason))
    elif command == BotApi.info_command:
      http_post = requests.post(BotApi.bot_api + self.send_message_method, data={'chatid': 454062609, 'text': str(infomation)})
      print "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason))
    elif command == BotApi.mem_command:
      http_post = requests.post(BotApi.bot_api + self.send_message_method, data={'chatid': 454062609, 'text': str(infomation)})
      print "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason))
    elif command == BotApi.check_site_status:
      http_post = requests.post(BotApi.bot_api + self.send_message_method, data={'chatid': 454062609, 'text': str(infomation)})
      print "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason)) + "\n"

  def get_command(self):
    system = SystemUtils()
    command = self.json_reponse['result'][-1]['message']['text']

    if command == BotApi.info_command:
      inf == system.get_info_server(command)
      information = inf._string()
      self.send_message(command, infomation)
    elif command == BotApi.load_command:
      load = system.get_load_server(command)
      self.send_message(command, load)
    elif command == BotApi.help_command:
      self.send_message(command, '')
    elif command == BotApi.mem_commmand:
      mem = system.get_mem_server(command)
      self.send_message(command, mem)
    elif command == BotApi.check_site_status:
      online_status = system.get_http_status(command)
      self.send_message(command, online_status)
    else:
      self.send_message(command, '')
      print "Nothing to send, error command"

  def get_auto_site_status(self):
    api_status = SystemUtils()
    while 1:
      try:
        api_status.get_http_status()
        time.sleep(5)
      except Exception as e:
        time.sleep(5)
        print str(e)
    
  def engine(self):
    while 1:
      try:
        self.get_command()
        time.sleep(5)
      except Exception as e:
        time.sleep(5)
        print str(e)

  def run_thread1(self):
    thread = threading.Thread(target=self.get_auto_site_status)
    thread.start()

  def run_thread2(self):
    thread = threading.Thread(target=self.engine)
    thread.start()

if __name__ == '__main__':

  print 'Starting BOT'
  obj = BotApi()
  obj.run_thread1()

  obj1 = BotApi()
  obj1.run_thread2()
