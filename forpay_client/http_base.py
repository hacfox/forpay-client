import base64
import hashlib
import random
import string
import time
from urllib.parse import urlencode

import requests
from Crypto.Hash import SHA256
from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5


class HttpClientBase(object):
    def __init__(self, app_id, key_id, private_key):
        self._app_id = app_id
        self._key_id = key_id
        self._private_key = private_key

    def _http_get(self, url, query_dict=None, proxies=None):
        set_auth_header = self.__set_auth_header(query_dict)

        headers = {}
        headers.update(set_auth_header)

        try:
            req = requests.session()
            req.proxies = proxies
            req.keep_alive = False
            response = req.get(url,
                               params=query_dict,
                               headers=headers,
                               timeout=5)

            if response.status_code in [200, 401]:
                reply = response.json()
                return reply, True

        except Exception as e:
            print(e)
        return {}, False

    def _http_post(self, url, body_dict=None, proxies=None):
        add_to_headers = self.__set_header(verb='POST', source_content=str(body_dict))

        headers = {}

        headers.update(add_to_headers)

        try:
            req = requests.session()
            req.proxies = proxies
            req.keep_alive = False
            response = req.post(url,
                                data=body_dict,
                                headers=headers,
                                timeout=5)

            if response.status_code in [200, 401]:
                reply = response.json()
                return reply, True

        except Exception as e:
            print(e)
        return {}, False

    def __set_auth_header(self, dict_param):
        encode_params = ''
        if dict_param:
            sorted_dict = sorted(dict_param.items(), key=lambda d: d[0])
            encode_params = urlencode(sorted_dict).replace("+", "%20").replace("*", "%2A").replace("%7E", "~")
        add_to_headers = self.__set_header(source_content=encode_params)
        return add_to_headers

    def __set_header(self, verb='GET', source_content=''):
        timestamp_str = get_million_timestamp()
        nonce = generate_random_str()

        b64md5 = get_b64md5(source_content)
        signature = self.__sign(verb, str(timestamp_str), self._app_id, nonce, b64md5)

        auth = 'SHA256-RSA {}:{}'.format(self._key_id, signature)
        header = init_header(timestamp_str, self._app_id, nonce)
        header['Authorization'] = auth
        return header

    def __sign(self, verb, timestamp_str, app_id, nonce, b64md5):
        sign_str = verb + '\n' \
                   + timestamp_str + '\n' \
                   + app_id + '\n' \
                   + nonce + '\n' \
                   + b64md5
        key = RSA.importKey(self._private_key)
        signer = PKCS1_v1_5.new(key)
        signature = signer.sign(SHA256.new(sign_str.encode("utf8")))
        return base64.b64encode(signature).decode("utf8")


def init_header(timestamp_str, app_id, nonce):
    header_dict = {
        'X-Request-Timestamp': str(timestamp_str),
        'X-Request-AppId': app_id,
        'X-Request-Nonce': str(nonce)
    }
    return header_dict


def get_b64md5(source=''):
    m = hashlib.md5()
    m.update(source.encode('utf8'))
    m_str = m.hexdigest()
    base_str = base64.b64encode(bytearray.fromhex(m_str))
    return base_str.decode('utf8')


def get_million_timestamp():
    t = time.time()
    return int(round(t * 1000))


def generate_random_str():
    random_length = random.randint(30, 32)
    str_list = [random.choice(string.digits + string.ascii_letters) for i in range(random_length)]
    random_str = ''.join(str_list)
    return random_str