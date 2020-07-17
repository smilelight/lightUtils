# -*- coding: utf-8 -*-
# @Time    : 2020/7/17 14:23
# @Author  : lightsmile
# @Software: PyCharm

from lightutils import inspect_variable, retrieve_name

if __name__ == '__main__':
    a = 3
    print(retrieve_name(a))
    print(inspect_variable(a))

