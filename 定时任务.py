# -*- coding: utf-8 -*-
# @Time     : 6/22/2021 21:24
# @Author   : Junyi
# @FileName: 定时任务.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import datetime
import schedule
import time
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
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options

# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')

# def func():
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y-%m-%d %H:%M:%S')
#     print('do func  time :',ts)

# def func2():
#     now = datetime.datetime.now()
#     ts = now.strftime('%Y-%m-%d %H:%M:%S')
#     print('do func2 time：',ts)
#
# schedule.every().day.at("10:30").do(job)

def timing():
    brower = webdriver.Chrome()
    try:
        brower.get(url='https://www.esports8.com/')

        brower.find_element_by_xpath('//div[@class="filterBox"]/a[1]').click()
        brower.find_element_by_xpath('//div[@class="right"]').click()

        response = brower.page_source
        print(response)
    finally:
        brower.close()

# def tasklist():
#     timing = []
#     schedule.clear()
#     schedule.every().day.at("10:30").do(job)
#
# tasklist()
if __name__ == '__main__':
    timing()