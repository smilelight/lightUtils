import json
import os


def read_json_line(filename: str, error_file: str=None):
    """
    从文件中逐行获取json对象
    :param filename: json文件名
    :param error_file: 保存错误信息的文件路径，若不指定则系统默认当前执行路径下`error.log`文件
    :return: json object 迭代器
    """
    if not error_file:
        error_file = os.path.abspath('.') + os.sep + 'error.log'
    with open(filename, encoding='utf-8') as f:
        line_count = 0
        for line in f:
            line_count += 1
            try:
                json_line = json.loads(line.strip())
                yield json_line
            except Exception as e:
                with open(error_file, 'a+', encoding='utf-8') as err_f:
                    err_f.write("line{}: {}".format(line_count, line))
                    continue
