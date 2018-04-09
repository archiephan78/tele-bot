#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- Alex -*-

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
        self.json_response = None

    bot_token = '574513532:AAFN3cEsV48DfFUv90wYhITiPb-nlFQ81Pg'
    api_url = 'https://api.telegram.org/bot'
    full_url = api_url + bot_token
    status_json = '/getUpdates'
    send_message_method = '/sendMessage'
    update_url = full_url + status_json
    user_id = 454062609

    load_command = "/load"
    info_command = "/info"
    help_command = "/help"
    mem_commmand = "/memory"

    def send_message(self, command, information):

        help_message = "Yon asked for /help"
        error_message = "Wrong command!"

        if command == BotApi.load_command:
            http_post = requests.post(BotApi.full_url + self.send_message_method, data={'chat_id': 454062609, 'text': str(information)})
            print "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason))
        elif command == BotApi.info_command:
            http_post = requests.post(BotApi.full_url + self.send_message_method, data={'chat_id': 454062609, 'text': str(information)})
            print "Response from Web-Server: \n"  + str((http_post.status_code, http_post.reason))
        elif command == BotApi.help_command:
            http_post = requests.post(BotApi.full_url + self.send_message_method, data={'chat_id': 454062609, 'text': help_message})
            print "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason))
        elif command == BotApi.mem_commmand:
            http_post = requests.post(BotApi.full_url + self.send_message_method, data={'chat_id': 454062609, 'text': str(information)})
            print  "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason))
        else:
            http_post = requests.post(BotApi.full_url + self.send_message_method, data={'chat_id': 454062609, 'text': str(error_message)})
            print "Response from Web-Server: \n" + str((http_post.status_code, http_post.reason)) + "\n"

    def get_command(self):
        path_to_file = os.getcwd()
        file_with_id = path_to_file + "/update_id_file.txt"

        with open(file_with_id, 'r') as myfile:
            last_id = myfile.read()
            myfile.close()

        offset = int(last_id)
        offset = int(offset) - 1

        values = {}
        values['offset'] = offset
        values['limit'] = '5'

        data = urllib.urlencode(values)
        response = urllib2.Request(self.update_url, data)
        response = urllib2.urlopen(response)
        block_from_json_response = response.read()

        self.json_response = json.loads(block_from_json_response)
        last_update_id_from_json = self.json_response['result'][-1]['update_id']
        last_user_id = self.json_response['result'][-1]['message']['from']['id']

        update_id_array = []
        for key in self.json_response['result']:
            update_id_array.append(key['update_id'])

        path_to_file = os.getcwd()
        file_with_id = path_to_file + "/update_id_file.txt"

        if os.path.exists(file_with_id):
            with open(file_with_id, 'r+') as myfile:
                last_update_id = myfile.read()

                if int(last_update_id) == int(last_update_id_from_json):
                    myfile.close()
                else:
                    myfile.read()
                    myfile.seek(0)
                    myfile.write(str(last_update_id_from_json))
                    myfile.close()

                    command = self.json_response['result'][-1]['message']['text']
                    system = SystemUtils()

                    if last_user_id == self.user_id:
                        if command == BotApi.info_command:
                            inf = system.get_info_server(command)
                            information = inf.to_string()
                            self.send_message(command, information)
                        elif command == BotApi.help_command:
                            self.send_message(command, '')
                        elif command == BotApi.load_command:
                            load = system.get_load_server(command)
                            self.send_message(command, load)
                        elif command == BotApi.mem_commmand:
                            mem = system.get_mem_server(command)
                            self.send_message(command, mem)
                        else:
                            self.send_message(command, '')
                            print "Nothing to send, error command has been entered"
                    else:
                        print "sad"
        else:
            print "File: " + file_with_id + " doesn't exist"

    def engine(self):
        while 1:
            try:
                self.get_command()
                time.sleep(1)
            except Exception, e:
                time.sleep(5)
                print str(e)

    def run_thread(self):
        thread = threading.Thread(target=self.engine)
        thread.start()

if __name__ == '__main__':

    print "Starting bot..."
    obj = BotApi()
    obj.run_thread()
