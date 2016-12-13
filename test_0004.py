#! /usr/bin/env python3
# -*- coding:utf-8 -*-

# 任一个英文的纯文本文件，统计其中的单词出现的个数。

import re
import collections

'''
从文件中读取内容，统计词频
'''
def count_word(path, *keywords):
    result = {}
    with open(path,'r', encoding='utf-8') as txt:
        all_the_text = txt.read()
        #大写转小写
        all_the_text = all_the_text.lower()
        #正则表达式替换特殊字符
        all_the_text = re.sub("\"|,|\.", "", all_the_text)

        for word in all_the_text.split():
            if (len(keywords) > 0 and word in keywords) or len(keywords) == 0:
                result[word] = result.get(word, 0) + 1
        return result

'''
以词频倒序
'''
def sort_by_count(d):
    # 字典排序
    d = collections.OrderedDict(sorted(d.items(), key = lambda x: -x[1]))
    return d

if __name__ == "__main__":
    path = 'The Golden Age.txt'
    dword = count_word(path, 'strummer', 'the', 'to')
    dword = sort_by_count(dword)
    for key, value in dword.items():
        print('%s:%s' %(key,value))