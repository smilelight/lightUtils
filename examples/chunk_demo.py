# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 15:07
# @Author  : lightsmile
# @Software: PyCharm

from lightutils import batch

if __name__ == '__main__':
    for item in batch(range(100)):
        print(item)
