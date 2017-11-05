#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
import requests
import json
import re
import time
import os
import base64
import binascii
from bs4 import BeautifulSoup
from Crypto.Cipher import AES
from pprint import pprint

# 验证信息
text = {
    'username': '',
    'password': '',
    'rememberLogin': 'true'
}

# def loadName():
#     global BASE_URL, headers
BASE_URL = 'http://music.163.com'
# 定义请求头
headers = {
    'Refer': 'http://music.163.com',
    'Host': 'music.163.com',
    'User-Agent': 'android',
    'Accept-Encoding': 'gzip',
    'Cookie': 'appver=4.1.3; os=android; osver=7.1.1; mobilename=ONEPLUS3010; resolution=1920x1080; channle=netease',
}

# Default_Header = {
#     'Referer': 'http://music.163.com/',
#     'Host': 'music.163.com',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:38.0) Gecko/20100101 Firefox/38.0 Iceweasel/38.3.0',
#                   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#                   'Accept-Encoding': 'gzip, deflate'
# }


# 加密信息
modulus = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
nonce = '0CoJUm6Qyw8W8jud'
pubKey = '010001'

# 函数部分


def aesEncrypt(text, secKey):
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    encryptor = AES.new(secKey, 2, '0102030405060708')
    ciphertext = encryptor.encrypt(text)
    ciphertext = base64.b64encode(ciphertext)
    return ciphertext.decode()


def rsaEncrypt(text, pubKey, modulus):
    text = text[::-1].encode()
    rs = int(binascii.hexlify(text), 16)**int(pubKey, 16) % int(modulus, 16)
    return format(rs, 'x').zfill(256)


def createSecretKey(size):
    return ''.join([hex(x)[2:] for x in os.urandom(size)])[0:16]


text = json.dumps(text)
secKey = createSecretKey(16)
encText = aesEncrypt(aesEncrypt(text, nonce), secKey)
encSecKey = rsaEncrypt(secKey, pubKey, modulus)
data = {
    'params': encText,
    'encSecKey': encSecKey
}

_session = requests.session()
_session.headers.update(headers)


if __name__ == '__main__':

    # TESTING!!!!!!!!!!!!111
    print('TESTING!!!!!!!!!!!!!!!!!!!!!!')
