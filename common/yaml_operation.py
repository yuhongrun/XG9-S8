import yaml
import requests
import json
#读取：
def read_yaml(file_name):
    with open(file_name, 'r',encoding='utf-8') as f:
        yaml_obj = yaml.load(f.read(),Loader=yaml.FullLoader)
        f.close()
        return yaml_obj
#读取提取文件：
def read_extract_yaml():
    with open('./yaml_file/extract_data.yaml', 'r',encoding='utf-8') as f:
        yaml_obj = yaml.load(f.read(),Loader=yaml.FullLoader)
        f.close()
        return yaml_obj
#写入
def wite_extract_yaml(data):
    with open('./yaml_file/extract_data.yaml','a',encoding='utf-8') as f:
        yaml.dump(data,f,allow_unicode=True)
        f.close()

#清空
def clear_extract_yaml():
    with open('./yaml_file/extract_data.yaml','w',encoding='utf-8') as f:
        f.truncate()
        f.close()


# def interface_request(method,url,data=None,header=None,**kwargs):
#     re = requests.request(method,url,data=data,headers=header)
#     return re

def interface_request(method,url,**kwargs):
    re = requests.request(method,url,**kwargs)
    return re


