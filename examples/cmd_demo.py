# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 16:21
# @Author  : lightsmile
# @Software: PyCharm

from lightutils import execute_cmd

if __name__ == '__main__':
    state, info = execute_cmd('ls')
    if state:
        print(info)
