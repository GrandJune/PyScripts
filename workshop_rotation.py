# -*- coding: utf-8 -*-
# @Time     : 8/17/2021 13:08
# @Author   : Junyi
# @FileName: workshop_rotation.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import random

person_list = ['junyi', 'yoda', 'jingqiao','guoting', 'jinya', 'xinyi', 'ginger','phoebe','yuening', 'Huangxin']
for i in range(5):
    group = random.sample(person_list, k=2)
    person_list = [each for each in person_list if each not in group]
    print(group)
