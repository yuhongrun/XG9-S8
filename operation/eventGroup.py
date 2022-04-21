from api.eventGroup import eventGroup
from common.logger import logger
from config import http_config
from core.result_base import ResultBase


def query_list(pageSize=None, pageIndex=None,):
    """
     01 事件组列表查询
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    data = {}
    pageInfo = {}
    json = {}
    if pageSize != 'None':
        pageInfo["pageSize"] = pageSize
    if pageIndex != 'None':
        pageInfo["pageIndex"] = pageIndex

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    res = eventGroup.query_list(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        logger.info("查询列表数据 ==>> 返回结果 ==>> {}".format(res.text))

    else:
        result.code = res.status_code
        result.error = "请求失败"
        result.response = res
    return result


def detail_id(id=None):

    """
    02
    事件组详情查询
    :id: 服务主键id
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    data = {}
    if id != 'None':
        data["id"] = id

    headers = http_config.param_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    res = eventGroup.detail_id(params=data, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        try:
            result.msg = res.json()["result"]
            result.success = True
        except:
            result.error = res.json()["msg"]


        # if res.json()["code"] == 0:
        #     result.success = True
        #     result.msg = res.json()["result"]
        # else:
        #     result.error = res.json()["msg"]
        result.response = res
        logger.info("id查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求失败"
    return result


def face_list(pageIndex=None, pageSize=None, eventGroupPid=None):
    # 03 事件组详情查询,关联服务列表查询
    """
    :pageSize:每页条数
    :pageIndex:页码
    :eventGroupPid:主键id
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if pageSize != 'None':
        pageInfo["pageSize"] = pageSize
    if pageIndex != 'None':
        pageInfo["pageIndex"] = pageIndex
    if eventGroupPid != 'None':
        data["eventGroupPid"] = eventGroupPid

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = eventGroup.face_list(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        logger.info("查询列表 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求失败"
    result.response = res
    return result


def add_update(id=None, eventGroupBid=None, servicePid=None, eventGroupName=None):
    # 04 事件组新增修改
    """
    :pageSize:每页条数
    :pageIndex:页码
    :eventGroupPid:主键id
    :return: 自定义的关键字返回结果 result
    """
    result = ResultBase()
    json = {}
    data = {}

    if id != 'None':
        data["id"] = id
    if eventGroupBid != 'None':
        data["eventGroupBid"] = eventGroupBid
    if servicePid != 'None':
        data["servicePid"] = servicePid
    if eventGroupName != 'None':
        data["eventGroupName"] = eventGroupName
    json["data"] = data

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = eventGroup.add_update(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["msg"]
        else:
            result.error = res.json()["msg"]
        logger.info("事件组新增更新 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求失败"
    result.response = res
    return result


def id_generate(servicePid, meteType):
    """
    事件组id生成
    :param servicePid: 服务pid
    :param metaType: 元模块类型
    :return:  自定义的关键字返回结果 result
    """

    result = ResultBase()
    json = {}
    data = {}
    if servicePid != 'None':
        data["servicePid"] = servicePid
    if meteType != 'None':
        data["meteType"] = meteType
    json["data"] = data
    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = eventGroup.id_generate(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        logger.info("事件组id生成 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求失败"
    result.response = res
    return result


def update_batch(ids, isDelete):
    """
    事件组批量更新字段接口
    :param ids: 服务pid
    :param isDelete: 元模块类型
    :return:  自定义的关键字返回结果 result
    """

    result = ResultBase()
    json = {}
    data = {}
    if ids != 'None':
        data["ids"] = ids
    if isDelete != 'None':
        data["isDeleted"] = isDelete
    json["data"] = data
    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = eventGroup.update_batch(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        try:
            result.msg = res.json()["result"]
            result.success = True
        except:
            try:
                result.error = res.json()["msg"]
            except:
                result.error = "返回异常"
        logger.info("事件组批量更新字段接口 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求失败"
    result.response = res
    return result
