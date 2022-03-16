# -*- coding: utf-8 -*-
# @Time     : 2022/3/16 21:51
# @Author   : Junyi
# @FileName: cut_video.py
# @Software  : PyCharm
# Observing PEP 8 coding style
import numpy as np
import cv2
import os
import time

START_HOUR = 0
START_MIN = 0
START_SECOND = 0
START_TIME = START_HOUR * 3600 + START_MIN * 60 + START_SECOND  # 设置开始时间(单位秒)
END_HOUR = 0
END_MIN = 19
END_SECOND = 50
END_TIME = END_HOUR * 3600 + END_MIN * 60 + END_SECOND  # 设置结束时间(单位秒)

video = r"C:\Users\Junee\Desktop\1.mp4"
cap = cv2.VideoCapture(video)
FPS = cap.get(cv2.CAP_PROP_FPS)
print(FPS)
FPS = 25
# size = (cap.get(cv2.CAP_PROP_FRAME_WIDTH), cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
size = (1920,1080)
print(size)
TOTAL_FRAME = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))  # 获取视频总帧数
frameToStart = START_TIME * FPS  # 开始帧 = 开始时间*帧率
print("frameToStart: ", frameToStart)
frametoStop = END_TIME * FPS  # 结束帧 = 结束时间*帧率
print("frametoStop: ", frametoStop)
videoWriter =cv2.VideoWriter(r'C:\Users\Junee\Desktop\1-c.avi',cv2.VideoWriter_fourcc('X','V','I','D'),FPS,size)

# cap.set(cv2.CAP_PROP_POS_FRAMES, frameToStart)  # 设置读取的位置,从第几帧开始读取视频
COUNT = 0
while True:
        success, frame = cap.read()
        if success:
            COUNT += 1
            if COUNT <= frametoStop and COUNT > frameToStart:  # 选取起始帧
                # print('correct= ', COUNT)
                videoWriter.write(frame)
        # print('mistake= ', COUNT)
        if COUNT > frametoStop:
            break
print('end')
