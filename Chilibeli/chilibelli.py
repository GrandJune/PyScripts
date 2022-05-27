# -*- coding: utf-8 -*-
# @Time     : 5/18/2022 20:27
# @Author   : Junyi
# @FileName: chilibelli.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import requests
import random
# from send_email import Sent_From_126
from lxml import etree
import time
import traceback
import csv
import re
import os
import shutil
import pandas as pd
# USER_AGENTS = [
#     "Mozilla/5.0 (Windows; U; MSIE 9.0; Windows NT 9.0; en-US)",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/523.15 (KHTML, like Gecko, Safari/419.3) Arora/0.3 (Change: 287 c9dfb30)",
#     "Mozilla/5.0 (X11; U; Linux; en-US) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3) Arora/0.6",
#     "Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.2pre) Gecko/20070215 K-Ninja/2.1.1",
#     "Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5",
#     "Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6",
#     "Opera/9.80 (Macintosh; Intel Mac OS X 10.6.8; U; fr) Presto/2.9.168 Version/11.52",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
#     "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36",
#     "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 (KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
#     'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 OPR/26.0.1656.60',
#     'Opera/8.0 (Windows NT 5.1; U; en)',
#     'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11'
# ]
USER_AGENTS = ["Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36"]
def parse():
    s = requests.Session()
    s.keep_alive = False  # 关闭长连接，防止连接次数过多
    s.adapters.DEFAULT_RETRIES = 10  # 重连接次数
    agent = random.choice(USER_AGENTS)
    # print('Agent: ',agent)
    s.headers = {'User-Agent': agent}
    response = s.get(url="https://mp.chilibeli.com/b2c/admin/login", timeout=10)  # 微博一定要带Cookie才行
    # print(response.text)
    post_data = {
        "phone": "896861593",
        "pass": "224b9426",
    }  # 登录POST所需参数
    cookie = {"auth": "75|fb7e27df6388748ca83a00a939dedf38|1652879077"}
    headers = {
        "referer": "https://mp.chilibeli.com/b2c/admin/login",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
        "origin": "https://mp.chilibeli.com",
        "sec-ch-ua-platform": "Windows"
    }
    respond_2 = s.post(url="https://mp.chilibeli.com/b2c/admin/login/first", data=post_data, cookies=cookie, headers=headers)
    respond_2.encoding = "utf-8"
    print("FIRST Text")
    print(respond_2.text)
    respond_3 = s.post(url="https://mp.chilibeli.com/b2c/admin/login/auth", data=post_data, cookies=cookie, headers=headers)
    print("AUTH Text")
    print(respond_3.text)
    respond_4 = s.get(url="https://mp.chilibeli.com/b2c/admin/", cookies=cookie, headers=headers)
    print("Admin Text")
    print(respond_4.text)
    return respond_2


if __name__ == '__main__':
    url_1 = 'https://mp.chilibeli.com/b2c/admin/login/first'
    url_2 = "https://mp.chilibeli.com/b2c/admin/login/auth"
    res = parse()
    # print(res.text)