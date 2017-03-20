# -*- coding: utf-8 -*-
# @Author: hades
# @Date:   2017-03-19 22:55:38
# @Last Modified by:   hades
# @Last Modified time: 2017-03-20 13:57:43
from __future__ import print_function
import os
import time
size = (217,67)

video = open(r"video.txt", "r")
time.sleep(20)
num = 1
for line in video:
    print(line,end='')
    if num % size[1] == 0:
        time.sleep(0.05)#系统休眠0.05秒防止闪屏
        os.system("clear")#清屏
    num += 1