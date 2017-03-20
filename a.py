# -*- coding: utf-8 -*-
# @Author: hades
# @Date:   2017-03-19 22:36:21
# @Last Modified by:   hades
# @Last Modified time: 2017-03-20 13:54:46
import numpy as np
import cv2

cap = cv2.VideoCapture('test.mp4')

num = 0
while (cap.isOpened()):
    print('pic',num)
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("img%d.png" % num, frame)
    num += 1
print('Done')