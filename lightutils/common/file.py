# -*- coding: utf-8 -*-
# @Time    : 2020/7/7 8:36
# @Author  : lightsmile
# @Software: PyCharm

import os
from typing import Union, List


class NotSpecifiedFileException(Exception):
    def __init__(self, info: Union[str, List[str]]):
        if isinstance(info, str):
            self._info = info
        else:
            self._info = '/'.join(info)

    def __str__(self):
        return "并非指定的文件错误，应该是形如：{}".format(self._info)


def check_file(file_path: str, ext: Union[str, List[str]] = None):
    if not os.path.exists(file_path):
        raise FileNotFoundError
    if ext and not file_path.endswith(ext):
        raise NotSpecifiedFileException('xx.' + ext)


if __name__ == '__main__':
    # check_file('fuck.txt', 'txt')
    # check_file('__init__.py', 'txt')
    check_file('__init__.py', 'py')
