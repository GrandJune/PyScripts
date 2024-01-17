# -*- coding: utf-8 -*-
# @Time     : 7/14/2021 21:32
# @Author   : Junyi
# @FileName: who_is_the_AE.py
# @Software  : PyCharm
# Observing PEP 8 coding style
from datetime import datetime

AE_list = ['Yihong Lan', 'Shahid M.N.', 'Dawei Chen', 'Junjie Zhou', 'Yonggang Li', 'Junyi Li', 'Ruilin Zhang', 'Kaile Lim']
reference_point = '2020-06-23'
current_time = datetime.now().strftime('%Y-%m-%d')
week_start = datetime.strptime(reference_point, '%Y-%m-%d')
week_end = datetime.strptime(current_time, '%Y-%m-%d')
gap = int(datetime.strftime(week_end, "%W")) - int(datetime.strftime(week_start, "%W"))
print(AE_list[gap % 8])