#! /usr/bin/env python3
# -*- coding:utf-8 -*-

import random
import string


def gene_activation_code(number, length=25):


    '''
    :param number: 生成的数量
    :param length: 激活码的长度
    :return:       返回激活码集合
    '''

    global result
    result = []
    source = string.ascii_uppercase + string.digits

    def create_code():
        code = "".join(random.sample(source, length))
        if code in result:
            code = create_code()
        return code

    result = [create_code() for i in range(number)]

    return result

if __name__ == "__main__":
    number = 3
    length = 25
    re = gene_activation_code(number)
    for r in re:
        print("gene：", r)

