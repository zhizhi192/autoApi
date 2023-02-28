import os
import yaml


class YamlUtil:
    # Todo：改成静态方法
    def read_case_yaml(self, case_name):
        with open(os.getcwd() + '/test_files/' + case_name, mode='r', encoding='utf-8') as f:
            for value in yaml.load(stream=f, Loader=yaml.FullLoader):
                yield value

    def write_extract_yaml(self, data):
        with open(os.getcwd() + '/extract.yaml', mode='a', encoding='utf-8') as f:
            yaml.dump(data=data, stream=f, allow_unicode=True)

    def read_extract_yamml(self, key):
        with open(os.getcwd() + '/extract.yaml', mode='r', encoding='utf-8') as f:
            value = yaml.load(stream=f, Loader=yaml.FullLoader)[key]
            return value

    def clean_extract_yaml(self):
        with open(os.getcwd() + '/extract.yaml', mode='w', encoding='utf-8') as f:
            f.truncate()
