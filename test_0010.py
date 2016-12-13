#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 使用 Python 生成字母验证码图片

from PIL import Image, ImageDraw, ImageFont, ImageFilter

import random


# 随机字母
def rnd_char():
    return chr(random.randint(65, 90))


# 随机颜色1
def rnd_color():
    return (random.randint(64, 265), random.randint(64, 265), random.randint(64, 265))


# 随机颜色2
def rnd_color2():
    return (random.randint(32, 127), random.randint(32, 127), random.randint(32, 127))

# 340 x 60:
width = 60 * 4
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象：
font = ImageFont.truetype('arial.ttf', 36)
# 创建Draw对象：
draw = ImageDraw.Draw(image)
# 填充每个像素
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rnd_color())

# 输出文字：
for t in range(4):
    draw.text((60 * t + 10, 10), rnd_char(), font=font, fill=rnd_color2())

# 模糊:
image = image.filter(ImageFilter.BLUR)
image.save('code.jpg', 'jpeg')
