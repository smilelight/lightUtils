import yaml

from ..common.file import check_file


def load_yaml(yml_path: str):
    check_file(yml_path, 'yml')
    return yaml.safe_load(open(yml_path, encoding='utf8'))
