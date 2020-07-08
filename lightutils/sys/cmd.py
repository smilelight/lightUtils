# -*- coding: utf-8 -*-
# @Time    : 2020/7/6 16:09
# @Author  : lightsmile
# @Software: PyCharm

import platform
import subprocess

encode_dict = {
    'Windows': 'gbk',
    'Linux': 'utf8'
}


def execute_cmd(cmd: str):
    try:
        process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        cmd_output = process.stdout.read().decode(encode_dict[platform.system()])
        return True, cmd_output
    except Exception:
        return False, None


if __name__ == '__main__':
    state, info = execute_cmd('ls')
    if state:
        print(info)
