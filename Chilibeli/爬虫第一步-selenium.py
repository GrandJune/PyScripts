# -*- coding: utf-8 -*-
# @Time     : 3/3/2021 13:24
# @Author   : Junyi
# @FileName: name_freq.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import csv
import sys
import pickle


class Data():
    def __init__(self):
        self.url_1 = 'https://mp.chilibeli.com/b2c/admin/login'
        self.url_2 = "https://mp.chilibeli.com/b2c/admin/login/first"
        self.url_3 = "https://mp.chilibeli.com/b2c/admin/login/auth"
        self.url_4 = "https://mp.chilibeli.com/b2c/admin/"
        self.url_5 = "https://mp.chilibeli.com/b2c/admin/coupon"  # Promo Code
        self.data = None
        self.username = "896861593"
        self.password = "224b9426"
        self.pages = ["https://mp.chilibeli.com/b2c/admin/coupon?&page=" + str(i) for i in range(250, 475)]
        self.flag = 0
        self.accumulative_flag = 0

    def login(self):
        chrome_options = Options()
        # chrome_options.add_argument('--headless')
        # chrome_options.add_argument('--disable-gpu')
        browser = webdriver.Chrome(options=chrome_options)
        browser.get(url=self.url_1)
        browser.find_element_by_id("username").send_keys(self.username)
        browser.find_element_by_id("password").send_keys(self.password)
        browser.find_element_by_xpath("//form/div[6]/button").click()
        # /html/body/div[3]/form/div[6]/button
        # print(brower.page_source)

        # with open(folder_path + r'\login_page.txt', 'w', encoding='utf-8', newline='') as outfile:
        #     outfile.write(browser.page_source)
        browser.get(url=self.url_4)
        # with open(folder_path + r'\admin_page.txt', 'w', encoding='utf-8', newline='') as outfile:
        #     outfile.write(browser.page_source)
        return browser

    def run_clawler(self):
            browser = self.login()
            pages = self.pages[self.accumulative_flag:]
            try:
                for page_index, page in enumerate(pages):  # 裁断了之后，坐标不一致
                    self.flag = page_index
                    print(page, self.accumulative_flag)
                    time.sleep(2)
                    browser.get(url=page)
                    time.sleep(2)
                    # with open(folder_path + r'\coupon_page_{0}.txt'.format(index), 'w', encoding='utf-8', newline='') as outfile:
                    #     outfile.write(browser.page_source)

                    edit_buttons = browser.find_elements_by_xpath("//tbody/tr/td[21]/a")
                    for click_index, each_button in enumerate(edit_buttons):
                        each_button.click()
                        time.sleep(2)
                        print("Click number: {0}/{1}".format(click_index, len(edit_buttons)))
                        # //*[@id="vue_order"]/div/div/div[3]/div[2]/table/tbody/tr[7]/td[21]/a
                        # //*[@id="vue_order"]/div/div/div[3]/div[2]/table/tbody/tr[1]/td[21]/a
                        folder_path = sys.path[0]
                        with open(folder_path + r'\data\edit_page_{0}_click_{1}.txt'.format(page_index+self.accumulative_flag+250, click_index+1), 'w', encoding='utf-8',
                                  newline='') as outfile:
                            outfile.write(browser.page_source)
                        close_button = browser.find_element_by_css_selector("div[class='modal-header']>button") # //*[@id="myModal1"]/div/div/div[1]/button
                        # unable to locate elements in the pop-up window
                        # use css selector -> can click the button now.  SO!!! CSS selector is superior to XPATH selector
                        # //*[@id="myModal1"]/div/div/div[1]/button
                        close_button.click()
                        time.sleep(2)
                        # print("Test point 3")
            except:
                browser.quit()
                self.accumulative_flag += self.flag
                time.sleep(60)
                self.run_clawler()
            finally:
                browser.quit()
            print("collection complete!")


    def clear(self):
        folder_path = sys.path[0]
        folder = folder_path + r'\data'
        data_files = []
        # for page_index in range(252, 475):
        #     for click_index in range(1, 21):  # C:\Users\workshop\Desktop\PyScripts\Chilibeli\data_2
        #         file_path = folder_path + r'\data\edit_page_{0}_click_{1}.txt'.format(page_index, click_index)
        #         print(page_index, click_index)
        #         if (page_index == 474) and (click_index >= 19):
        #             pass
        #         else:
        #             data_files.append(file_path)
        #
        # # print(data_files)
        # data_result = []
        # for each_file in data_files:
        #     # each_file = r"C:\Users\workshop\Desktop\PyScripts\Chilibeli\data_2\edit_page_1_click_19.txt"
        #     parser = etree.HTMLParser(encoding="utf-8")
        #     tree = etree.parse(each_file, parser=parser)
        #     user_list = tree.xpath("//div/span/text()")  # //*[@id="user62555"]
        #     user_list = [each for each in user_list if each != '\n ']
        #     user_list = [each.replace('\n', " ") for each in user_list]
        #     print(user_list)
        #     data_result.append(user_list)
        # print(len(data_result))  # 字符串里面带有\n 导致多出来26行
        # with open("user_list_data_2", "wb") as outfile:
        #     pickle.dump(data_result, outfile)
        infile_1 = open("user_list_data", 'rb')
        result_1 = pickle.load(infile_1)
        infile_1.close()
        print(len(result_1))
        infile_2 = open('user_list_data_2', 'rb')
        result_2 = pickle.load(infile_2)
        infile_2.close()
        print(len(result_2))
        result = result_1 + result_2
        print(len(result))
        with open("user_list.csv", 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            for each_line in result:
                writer.writerow(each_line)

        # //*[@id="user62555"]/span

if __name__ == '__main__':
    data = Data()
    # data.run_clawler()
    data.clear()