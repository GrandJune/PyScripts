# -*- coding: utf-8 -*-
# @Time     : 2022/3/16 22:11
# @Author   : Junyi
# @FileName: movie-cut.py
# @Software  : PyCharm
# Observing PEP 8 coding style
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_hour = 0
start_min = 28
start_second = 00
start_time = start_hour * 3600 + start_min * 60 + start_second  # 设置开始时间(单位秒)

end_hour = 0
end_min = 49
end_second = 00
end_time = end_hour * 3600 + end_min * 60 + end_second
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
inflie_path = r"C:\Users\Junee\Downloads\GMT20220405-104514_Recording_3440x1440.mp4"
outfile_path = "Not Economists-Treatsure.mp4"
ffmpeg_extract_subclip(inflie_path, start_time, end_time, targetname=outfile_path)