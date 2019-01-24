import hashlib
import random

import requests
from .config import CONFIG

app_key = CONFIG["appKey"]
secret_key = CONFIG["secretKey"]
QUERY_URL = 'http://openapi.youdao.com/api'


class YDTranslater:
    def __init__(self, appKey=app_key, secretKey=secret_key):
        self.appKey = appKey
        self.secretKey = secretKey

    def get_sign(self, q):
        salt = str(random.randint(1, 65536))
        sign = self.appKey + q + salt + self.secretKey
        m = hashlib.md5()
        m.update(sign.encode())
        md5_sign = m.hexdigest()
        return salt, md5_sign

    def query(self, q, from_lang='EN', to_lang='zh-CHS'):
        salt, sign = self.get_sign(q)
        query_para = {
            'q': q,
            'from': from_lang,
            'to': to_lang,
            'appKey': self.appKey,
            'salt': salt,
            'sign': sign
        }
        try:
            result = requests.get(QUERY_URL, params=query_para, timeout=5)
            if result.status_code == 200:
                return result.json()
            else:
                return 'Error'
        except:
            return 'Error'
