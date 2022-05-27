# -*- coding: utf-8 -*-
# @Time     : 3/3/2021 13:24
# @Author   : Junyi
# @FileName: name_freq.py
# @Software  : PyCharm
# Observing PEP 8 coding style
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from lxml import etree
import csv
import sys


class Data():
    def __init__(self, none_value=None):
        self.url = 'https://forebears.io/indonesia/forenames'
        self.data = None
        self.none_value = none_value

    def run_clawler(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument('--headless')
            chrome_options.add_argument('--disable-gpu')
            brower = webdriver.Chrome(options=chrome_options)
            brower.get(url=self.url)
            print(brower.page_source)
            folder_path = sys.path[0]
            with open(folder_path + r'\page.txt', 'w', encoding='utf-8', newline='') as outfile:
                outfile.write(brower.page_source)
            print("collection complete!")
        finally:
            brower.close()

    def clean_data(self):
        folder_path = sys.path[0]
        parser = etree.HTMLParser(encoding="utf-8")
        tree = etree.parse(folder_path + r'\page.txt', parser=parser)
        forename = tree.xpath('//tbody/tr/td[3]/a/text()')
        # print("forename: ", forename)
        forename = [each for each in forename if each not in self.none_value]
        gender = tree.xpath('//tbody/tr/td[2]/div/text()')
        gender_flag = tree.xpath('//tbody/tr/td[2]/div/@class')
        combinations = [[i, j] for [i, j] in zip(gender, gender_flag)]
        gender_clear = [["None", "None"]] * 1000  # [male, female]
        count = 0
        for each in combinations:
            if each[0] == '100%':
                if each[1] == 'f':
                    gender_clear[count] = ["None", "100"]
                else:
                    gender_clear[count] = ["100", "None"]
                count += 1
            elif each[0] == '\xa0':
                pass
            else:
                if each[1] == 'f':
                    gender_clear[count] = ["None", each[0].replace("%", "")]
                else:
                    gender_clear[count] = [each[0].replace("%", ""), "None"]
                count += 1
        # print("gender_clear: ", gender_clear)
        self.data = [[i] + j for [i, j] in zip(forename, gender_clear)]

        for each in self.data:
            if (each[1] == "None") and (each[2] == "None"):
                pass
            elif each[1] == "None":
                each[1] = str(100-int(each[2]))
            elif each[2] == "None":
                each[2] = str(100-int(each[1]))
        missing_data = [[i, "50", "50"] for i in self.none_value]
        self.data += missing_data
        print("Data: ", self.data)

    def output(self):
        folder_path = sys.path[0]
        header = ["Forename", "Male", "Female"]
        with open(folder_path + r'\data.csv', 'w', encoding='utf-8', newline='') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(header)
            for eachline in self.data:
                writer.writerow(eachline)
        print("Output completed!")


if __name__ == '__main__':
    none_value = ['La', "St", "Anah", 'Saepudin', 'Acih', 'Ikah', 'Enah', 'Maesaroh', 'Ajat', 'Binti', 'Usup', 'Jaenudin']
    data = Data(none_value=none_value)
    # data.run_clawler()
    data.clean_data()
    data.output()