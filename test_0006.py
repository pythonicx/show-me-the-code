#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

from test_0004 import *
import os


def search_txt(path=os.getcwd()+'\\''txt'):
    txt_paths = []
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
        # 判断是否为文件并以 .txt 结尾
        if os.path.isfile(new_path) and new_path.endswith('.txt'):
            txt_paths.append(new_path)
        # 判断是否为文件夹
        elif os.path.isdir(new_path):
            txt_paths.extend(search_txt(new_path))
    return txt_paths


def get_key_word(paths, top=3):
    dict = {}
    for path in paths:
        print('path:', path)
        keyword = {}
        # 获取文件名, 不包含后缀
        file_name = path.split("\\")[-1].split(".")[0]
        dword = sort_by_count(count_word(path))
        i = 0
        for k, v in dword.items():
            keyword[k] = v
            i+=1
            if i == top:
                break
        dict[file_name] = keyword
    return dict

if __name__ == "__main__":
    t = search_txt()
    dict = get_key_word(t, top=1)
    for k, v in dict.items():
        print('【%s】的关键字如下：'% k)
        for x, z in v.items():
            print('%s:%s' %(x, z))