# -*- coding: utf-8 -*-
# @Time     : 2022/3/16 22:11
# @Author   : Junyi
# @FileName: movie-cut.py
# @Software  : PyCharm
# Observing PEP 8 coding style
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
start_hour = 0
start_min = 20
start_second = 5
start_time = start_hour * 3600 + start_min * 60 + start_second  # 设置开始时间(单位秒)

end_hour = 0
end_min = 39
end_second = 40
end_time = end_hour * 3600 + end_min * 60 + end_second
# ffmpeg_extract_subclip("full.mp4", start_seconds, end_seconds, targetname="cut.mp4")
inflie_path = r"C:\Users\Junee\Desktop\67-cut.mp4"
outfile_path = "7-cut.mp4"
ffmpeg_extract_subclip(inflie_path, start_time, end_time, targetname=outfile_path)