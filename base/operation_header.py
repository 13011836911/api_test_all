"""
__time__:2021/2/2 11:17
__author__:songshijie
"""

import requests
import json
from base.operation_json import OperationJson

class OperationHeader:
    global cookie

    def write_cookie(self):
        url_login = 'https://nx-v8-g1-trail.ntalker.com/platform/user/login'
        data = {
            'loginId': 'songshijie',
            'password': 'xiaoneng0924'
        }
        jsonData = json.dumps(data)
        cookie_jar = requests.post(url_login, jsonData).cookies
        cookie = requests.utils.dict_from_cookiejar(cookie_jar)
        opera_json = OperationJson('../json_config/cookie.json')
        opera_json.write_data(json.dumps(cookie))

