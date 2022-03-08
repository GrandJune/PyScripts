# -*- coding: utf-8 -*-
# @Time     : 9/11/2021 14:14
# @Author   : Junyi
# @FileName: TA-grading.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import csv


folder_path = r'C:\Users\workshop\OneDrive - National University of Singapore\TA-BT2101-Econometrics\uploads'
in_file_path = folder_path + r'\PS1.csv'
out_file_path = folder_path + r'\PS1_2.csv'

data = []
with open(in_file_path, 'r', encoding='utf-8', newline='') as infile:
    reader = csv.reader(infile)
    for eachline in reader:
        # print(eachline)
        comments = '[Question 1]\n' + eachline[1] + '\n' + 'Question 2\n' + eachline[2]
        data.append([eachline[0], eachline[-1],'', comments,])

# print(data)
with open(out_file_path,'w', encoding='utf-8',newline='') as out_file:
    writer = csv.writer(out_file)
    writer.writerows(data)

