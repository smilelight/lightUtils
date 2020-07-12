# -*- coding: utf-8 -*-
# @Time    : 2020/6/29 15:07
# @Author  : lightsmile
# @Software: PyCharm

from lightutils import batch, cutoff_iter

if __name__ == '__main__':

    # test batch
    for item in batch(range(100)):
        print(item)

    # test cutoff_ter
    for item in cutoff_iter(range(20)):
        print(item)
