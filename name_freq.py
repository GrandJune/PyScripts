# -*- coding: utf-8 -*-
# @Time     : 6/22/2021 21:24
# @Author   : Junyi
# @FileName: 爬取开赛时间和链接.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import csv
import sys
import time
import re
# from send_email import Sent_From_126
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
import datetime
import schedule

chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')


def task_fun():
    result = {}    # {'URL': 'Time'}
    try:
        brower = webdriver.Chrome(options=chrome_options)
        brower.get(url='https://forebears.io/indonesia/forenames')
        # print(brower.page_source)
        gender = brower.find_elements_by_css_selector(
            "table tbody tr :nth-child(2)")
        i = 0
        gender_f = []
        gender_m = []
        for each in gender:
            f_flag = each.find_elements_by_css_selector("div [class='f']")
            m_flag = each.find_elements_by_css_selector("div [class='m']")
            m_full_flag = each.find_elements_by_css_selector("div [class='m full']")
            if f_flag and m_flag:
                # print(f_flag[0].text)
                gender_f.append(f_flag[0].text)
                gender_m.append(m_flag[0].text)
            elif m_flag:
                # print(m_flag[0].text)
                gender_f.append("None")
                gender_m.append(m_flag[0].text)
            elif f_flag:
                # print(m_flag[0].text)
                gender_f.append(f_flag[0].text)
                gender_m.append("None")
            elif m_full_flag:
                gender_f.append(0)
                gender_m.append(m_full_flag[0].text)
            else:
                gender_f.append("None")
                gender_m.append("None")
        for a, b in zip(gender_f, gender_m):
            print(a, b)
        print(len(gender_f), len(gender_m))
        # genders_f = brower.find_elements_by_css_selector(
        #     "table tbody tr :nth-child(2) div[class='f']")
        # genders_m = brower.find_elements_by_css_selector(
        #     "table tbody tr :nth-child(2) div[class='m']")
        # print(len(genders_f))
        # print(len(genders_m))


        # for each in genders_f:
        #     print(each.text)
        # forenames = brower.find_elements_by_css_selector(
        #     "table tbody tr td[class='sur']")
        # incidences = brower.find_elements_by_css_selector(
        #     "table tbody tr :nth-child(4)")
        # frequencies = brower.find_elements_by_css_selector(
        #     "table tbody tr :nth-child(5)")

        # data = []
        # for rank, gender, forename, incidence, frequency in zip(ranks, genders, forenames, incidences, frequencies):
        #     data.append([rank, gender, forename, incidence, frequency])
        # folder_path = sys.path[0]
        # with open(folder_path + r'\name_freq.csv', 'w', encoding='utf-8', newline='') as outfile:
        #     writer = csv.writer(outfile)
        #     writer.writerows(result.items())
        # print("complete!")
    finally:
        brower.close()

if __name__ == '__main__':
    task_fun()