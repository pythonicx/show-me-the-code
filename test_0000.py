#! /usr/bin/env python3
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont
import random

# 打开一个图形文件
im = Image.open(r'C:\Users\Gamer\Desktop\phone\QQ图片20160919214417.jpg')
txt = 111111111111
w, h = im.size
font = ImageFont.truetype('Arial.ttf', 80)
draw = ImageDraw.Draw(im)
color = (255, 0, 0)
draw.text((w-(80 / 2 * len(str(txt))), 0), str(txt), font=font, fill=color)
im.save('0000.jpg', 'jpeg')