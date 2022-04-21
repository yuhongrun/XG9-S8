from api.InteractiveManagement import interactive_Management
from common.logger import logger
from config import http_config
from core.result_base import ResultBase

# 定义一个
def query_details_by_id(idList=None, pageIndex=None, pageSize=None):
    result = ResultBase()

    # id_list: [
    #     381,
    #     378
    # ]
    data = {}
    pageInfo = {}
    json = {}
    if idList != 'None':
        data["idList"] = idList
    if pageIndex != 'None':
        pageInfo["pageIndex"] = pageIndex
    if pageSize != 'None':
        pageInfo["pageSize"] = pageSize
    json["data"] = data
    json["pageInfo"] = pageInfo
    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = interactive_Management.query_details_by_id(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("获取交互接口列表==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result

def get_interactive_interface_list(category=None, pageIndex=None, pageSize=None, interfaceName=None, interfaceBid=None,
                                   modelCodeList=None):
    result = ResultBase()
    json = {}
    pageInfo={}
    data = {}

    if category != 'None':
        data["category"] = category
    if interfaceName != 'None':
        data["interfaceName"] = interfaceName
    if interfaceBid != 'None':
        data["interfaceBid"] = interfaceBid
    if pageIndex != 'None':
        pageInfo["pageIndex"] = pageIndex
    if pageSize != 'None':
        pageInfo["pageSize"] = pageSize
    if modelCodeList != 'None':
        data["modelCodeList"] = modelCodeList
    json["data"] = data
    json["pageInfo"] = pageInfo
    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = interactive_Management.get_interactive_interface_list(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("获取交互接口列表==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


