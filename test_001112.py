#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'''
0011:敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
0012:敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''

import re
import os


class Filtered(object):

    def __init__(self, list):
        self.filter = list

    def set_text(self, text):
        self.text = 'Freedom' if text in self.filter else 'Human Rights'

    def get_text(self):
        return self.text


def get_filtered(path='filtered_words.txt'):
    result = []
    with open(path) as txt:
        for line in txt.readlines():
            result.append(line.strip())
    return result


class cNode(object):
    def __init__(self):
        self.children = None


# The encode of word is UTF-8
# The encode of message is UTF-8
class cDfa(object):
    def __init__(self, lWords):
        self.root = None
        self.root = cNode()
        for sWord in lWords:
            self.addWord(sWord)

    # The encode of word is UTF-8
    def addWord(self, word):
        node = self.root
        iEnd = len(word) - 1
        for i in range(len(word)):
            if not node.children:
                node.children = {}
                if i != iEnd:
                    node.children[word[i]] = (cNode(), False)
                else:
                    node.children[word[i]] = (cNode(), True)

            elif word[i] not in node.children:
                if i != iEnd:
                    node.children[word[i]] = (cNode(), False)
                else:
                    node.children[word[i]] = (cNode(), True)
            else:  # word[i] in node.children:
                if i == iEnd:
                    Next, bWord = node.children[word[i]]
                    node.children[word[i]] = (Next, True)

            node = node.children[word[i]][0]

    def isContain(self, sMsg):
        root = self.root
        iLen = len(sMsg)
        for i in range(iLen):
            p = root
            j = i
            while (j < iLen and p.children != None and sMsg[j] in p.children):
                (p, bWord) = p.children[sMsg[j]]
                if bWord:
                    return True
                j += 1
        return False

    def filter(self, sMsg):
        lNew = []
        root = self.root
        iLen = len(sMsg)
        i = 0
        bContinue = False
        while i < iLen:
            p = root
            j = i
            while (j < iLen and p.children != None and sMsg[j] in p.children):
                (p, bWord) = p.children[sMsg[j]]
                if bWord:
                    # print sMsg[i:j+1]
                    lNew.append(u'*' * (j - i + 1))  # 关键字替换
                    i = j + 1
                    bContinue = True
                    break
                j += 1
            if bContinue:
                bContinue = False
                continue
            lNew.append(sMsg[i])
            i += 1
        return ''.join(lNew)

if __name__ == "__main__":
    f = get_filtered()
    filtered = Filtered(f)
    print(filtered.filter)
    input = input('请输入：')
    filtered.set_text(input)
    print(filtered.get_text())

    dfa = cDfa(f)
    print(dfa.filter(input+'欢迎您'))