# -*- coding: utf-8 -*-
# @Author: hades
# @Date:   2017-03-19 22:37:42
# @Last Modified by:   hades
# @Last Modified time: 2017-03-20 14:20:30
from PIL import Image

size = (217,67)#终端的大小

def resize_pic(img):
    im = Image.open(img, 'r').convert("L")
    im = im.resize(size)
    return im

def pic_to_char(num):
    video = open("video.txt", "w")
    for i in range(num):
        im = resize_pic('img%d.png' % i)
        for y in range(size[1]):
            for x in range(size[0]):
                color = ' ' if im.getpixel((x, y))>210 else '*' 
                video.write(color)
            video.write("\n")
        print(i)
    video.close()
    print('Done')
pic_to_char(2157);#图片的数量