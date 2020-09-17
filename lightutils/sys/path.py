# -*- coding: utf-8 -*-
import os
import sys

from ..common.file import get_file_name
from ..common.log import logger


def add_sys_path(file_path: str, project_name: str):
    if not os.path.exists(file_path):
        raise FileNotFoundError("{} not found".format(file_path))
    flag = False
    parent_path = os.path.abspath(file_path)
    parent_name = get_file_name(parent_path)
    project_path = None
    while parent_name:
        parent_path = os.path.dirname(parent_path)
        for child_name in os.listdir(parent_path):
            if child_name == project_name:
                flag = True
                project_path = parent_path
                break
        if flag:
            break
    if flag:
        sys.path.insert(0, project_path)
        logger.info("已成功将{}添加至系统路径".format(project_path))
    else:
        raise FileNotFoundError("{} not found".format(project_name))

