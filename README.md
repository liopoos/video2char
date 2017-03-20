# video2char

## 将视频变成字符动画的py脚本。

![WechatIMG23](https://oavi5ezjr.qnssl.com/wp-content/uploads/2017/03/WechatIMG23.jpg)

# 引入模块

需要Python的两个模块

opencv #读取视频，将视频保存成一帧一帧的图片。

```python
pip install opencv-python
```

pillow #图像处理，将图片转换成字符。

```python
pip install pillow
```



# 读取视频

**a.py**

```
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

```

a.py将视频进行解析，把每一帧导出一张图片，格式为img%d.png。

![2017-03-20 14_33_01](https://oavi5ezjr.qnssl.com/wp-content/uploads/2017/03/2017-03-20-14_33_01.gif)

# 处理图片

**b.py**

```
# -*- coding: utf-8 -*-
# @Author: hades
# @Date:   2017-03-19 22:37:42
# @Last Modified by:   hades
# @Last Modified time: 2017-03-20 13:55:23
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

```

将每一张图片进行处理，Image.open()用来读取图片，convert(“L”)把它转换为灰度图。im.getpixel()接受一个二元组(x,y)，返回坐标为x,y的像素的颜色，因为这里是灰度图，所以返回值是一个整数。所有的字符将存储在video.txt文件下。

![2017-03-20 14_21_43](https://oavi5ezjr.qnssl.com/wp-content/uploads/2017/03/2017-03-20-14_21_43.gif)

# 播放字符

**c.py**

```
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
num = 1
for line in video:
    print(line,end='')
    if num % size[1] == 0:
        time.sleep(0.05)#系统休眠0.05秒防止闪屏
        os.system("clear")#清屏
    num += 1

```

 

系统读入video.txt，每次读取67行，并迭代输出每一行，之后系统休眠0.05秒，清除屏幕，并进行下一次输出，直到文件全部输出完毕。

要注意的是，size的比例要和视频保持一致，大小要和你的终端保持一致，这样才能完整显示。



