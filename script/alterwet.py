# -*- coding:utf-8 -*-
import logformat
import requests
import json


class Comp(object):
    def __init__(self, tor, message, logger):
        self._comp_id = "wwca9e177a69dcdecc"
        self._secret = "x8G9ve4HZr3EDUjz8NfX5xZUCsDpwuo3E_KV_MDz27g"
        self._agent_id = 1000003
        self._token = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'.format(self._comp_id,
                                                                                                    self._secret)
        self._tor = tor
        self._message = message
        self._logger = logger
        self._filename = 'AlterComWet'

    def logger(self):
        lg = logformat.Logger(logger=self._logger, filename=self._filename)
        return lg

    def conn(self):
        try:
            request = requests.get(self._token)
            access_token = request.json()['access_token']
        except Exception as e:
            self.logger().info(str(e))
        else:
            global msg_url
            msg_url = 'https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}'.format(access_token)
        return msg_url

    def format(self):
        params = {"touser": self._tor,
                  # "toparty": toparty,
                  "msgtype": "text",
                  "agentid": self._agent_id,
                  "text": {"content": self._message},
                  "safe": 0
                  }
        return params

    def post(self):
        try:
            requests.post(self.conn(), data=json.dumps(self.format()))
        except Exception as e:
            self.logger().info(str(e))
        else:
            self.logger().info(
                'Sending a successful company WeChat' + 'sendto：' + self._tor + ';;message：' + self._message)
