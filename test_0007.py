#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

from test_0004 import *
import os
import re


def search_py(path=os.getcwd()):
    py_paths = []
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
        # 判断是否为文件并以 .py 结尾
        if os.path.isfile(new_path) and new_path.endswith('.py'):
            py_paths.append(new_path)
        # 判断是否为文件夹
        elif os.path.isdir(new_path):
            py_paths.extend(search_py(new_path))
    return py_paths


def count_code(paths):
    code, blank, comment = (0, 0, 0)
    comment_flag = False
    for path in paths:
        comment_flag = False
        with open(path, 'r', encoding='utf-8') as py:
            for line in py.readlines():
                line = line.strip()
                if len(line) == 0:
                    blank += 1
                elif line.startswith('#'):
                    comment += 1
                elif comment_flag:
                    comment += 1
                    if line.startswith("'''") or line.startswith('"""'):
                        comment_flag = False
                elif line.startswith("'''") or line.startswith('"""'):
                    comment += 1
                    if not ((line.endswith("'''") or line.endswith('"""')) and len(line) > 3):
                        comment_flag = True
                else:
                    code += 1
    return code, blank, comment

if __name__ == "__main__":
    t = search_py()
    code, blank, comment = count_code(t)
    print('''
        code:%s
        blank:%s
        comment:%s
    ''' %(code, blank, comment))