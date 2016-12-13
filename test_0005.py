#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

import os
import imghdr
from PIL import Image


def search_img(path=os.getcwd()+'\\''img'):
    img_paths = []
    # 判断路径是否存在
    if not os.path.exists(path):
        print('is None:', path)
        return None;

    # 判断路径是否是文件夹
    if not os.path.isdir(path):
        print('not dir:', path)
        return None;
    new_path = ''
    # 遍历文件
    for x in os.listdir(path):
        new_path = os.path.join(path, x)
        # 判断是否为文件并是图片文件
        if os.path.isfile(new_path) and imghdr.what(new_path):
            img_paths.append(new_path)
        # 判断是否为文件夹
        elif os.path.isdir(new_path):
            img_paths.extend(search_img(new_path))
    return img_paths


def cut_img(source, width=1136, height=640):
    TARGET_PATH = os.getcwd()+'\\'+'cutImg'
    for path in source:
        print('path:', path)
        # 获取文件名
        file_name = path.split("\\")[-1]
        file_type = imghdr.what(path)
        # 打开一个jpg图像文件，注意是当前路径:
        im = Image.open(path)
        # 获得图像尺寸:
        w, h = im.size
        w = min(w, width)
        h = min(h, height)
        print(w,h)
        im.thumbnail((w, h))
        # 把缩放后的图像用jpeg格式保存:
        target = TARGET_PATH + '\\' + file_name
        print('target:', target)
        im.save(target, file_type)

if __name__ == "__main__":
    s = search_img()
    cut_img(s)