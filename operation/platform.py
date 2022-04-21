from api.platform import platform
from common.logger import logger
from config import http_config
from core.result_base import ResultBase


# 01_查询架构平台
# page_index,page_size,platformName,except_code,except_result,except_testcase_description
def getPlatformList(page_index=None, page_size=None, platformName=None):
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if page_index != 'None':
        pageInfo["pageIndex"] = page_index
    if page_size != 'None':
        pageInfo["pageSize"] = page_size
    if platformName != 'None':
        data["platformName"] = platformName
    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.getPlatformList(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


#  02_更新平台架构
def updatePlatform(id=None, paltformCnName=None, platformName=None, description=None):
    result = ResultBase()
    json = {}
    data = {}

    if id != 'None':
        data["id"] = id
    if paltformCnName != 'None':
        data["platformCnName"] = paltformCnName
    if platformName != 'None':
        data["platformName"] = platformName
    if description != 'None':
        data["description"] = description
    json["data"] = data

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.updatePlatform(json=json, headers=headers)
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
        logger.info("编辑 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    result.response = res
    return result


#   03_更新逻辑域
# id domainName domainCnName description platformPid except_code except_result ,except_testcase_description
def updateDomain(id=None, domainName=None, domainCnName=None, description=None, platformPid=None):
    result = ResultBase()
    json = {}
    data = {}
    if id != 'None':
        data["id"] = id
    if domainName != 'None':
        data["domainName"] = domainName
    if domainCnName != 'None':
        data["domainCnName"] = domainCnName
    if description != 'None':
        data["description"] = description
    if platformPid != 'None':
        data["platformPid"] = platformPid
    json["data"] = data
    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.updateDomain(json=json, headers=headers)
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
        # if res.json()["code"] == 0:
        #     result.success = True
        #     result.msg = res.json()["result"]
        # else:
        #     result.error = res.json()["msg"]
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    result.response = res
    return result


#   04_获取逻辑域列表
# page_index, page_size ,except_code, except_result ,except_testcase_description
def getDomainList(page_index=None, page_size=None, platformPid=None, domainName=None):
    """
    04_获取逻辑域列表
    :param page_index:
    :param page_size:
    :param platformPid:
    :param domainName:
    :return:
    """
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if page_index != 'None':
        pageInfo["pageIndex"] = page_index
    if page_size != 'None':
        pageInfo["pageSize"] = page_size
    if platformPid != 'None':
        data["platformPid"] = platformPid
    if domainName != 'None':
        data["domainName"] = domainName

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.getDomainList(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("获取逻辑域列表 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 05_获取逻辑域列表
# page_index, page_size ,except_code, except_result ,except_testcase_description
def getLogicSystemList(page_index=None, page_size=None, domainPid=None, platformPid=None, subSysName=None ):
    result = ResultBase()
    json = {}
    pageInfo = {}
    data = {}

    if page_index != 'None':
        pageInfo["page_index"] = page_index
    if page_size != 'None':
        pageInfo["page_size"] = page_size
    if domainPid != 'None':
        data["domainPid"] = domainPid
    if platformPid != 'None':
        data["platformPid"] = platformPid
    if subSysName != 'None':
        data["subSysName"] = subSysName

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.getLogicSystemList(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        logger.info("获取逻辑域列表 ==>> 返回结果 ==>> {}".format(res.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    result.response = res
    return result


# 06_子系统新增更新接口
# domain_pid,subSysType,subSysCnNam,subSysNam,except_code, except_result ,except_testcase_description
def addOrUpdateLogicSystem(id=None,domain_pid=None, subSysType=None, subSysCnName=None, subSysName=None,description=None):
    """
    添加更新逻辑子系统
    :param id:
    :param domain_pid:
    :param subSysType:
    :param subSysCnName:
    :param subSysName:
    :param description:
    :return:
    """
    result = ResultBase()
    json = {}
    data = {}
    if id != 'None':
        data["id"] = id
    if domain_pid != 'None':
        data["domainPid"] = domain_pid
    if subSysType != 'None':
        data["subSysType"] = subSysType
    if subSysCnName != 'None':
        data["subSysCnName"] = subSysCnName
    if subSysName != 'None':
        data["subSysName"] = subSysName
    if description != 'None':
        data["description"] = description
    json["data"] = data

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.addOrUpdateLogicSystem(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("子系统新增更新接口 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


# 07_子系统详情接口
# id,except_code,except_result,except_testcase_description
def getLogicSystemDetail(id=None):
    result = ResultBase()
    # json = {}
    # data = {}
    #
    # if id != 'None':
    #     data["id"] = id
    # json["data"] = data

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.getLogicSystemDetail(id, headers=headers)
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
        logger.info("子系统详情接口 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求失败"
    return result


# 08_删除子系统接口
# id,except_code,except_result,except_testcase_description
def batchUpdateField(ids=None, isDeleted=None):
    """
    删除子系统接口
    :param ids:
    :param isDeleted:
    :return:
    """
    result = ResultBase()
    json = {}
    data = {}

    if ids != 'None':
        data["ids"] = ids
    if isDeleted != 'None':
        data["isDeleted"] = isDeleted
    json["data"] = data

    headers = http_config.json_header
    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = platform.batchUpdateField(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("08_删除子系统接口 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result