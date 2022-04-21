from api.services import services
from common.logger import logger
from config import http_config
from core.result_base import ResultBase


# 服务详情

def getMetaServiceDetail(id=None):
    result = ResultBase()

    headers = http_config.param_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.getMetaServiceDetail(id, headers=headers)
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


def getMetaServiceList(pageIndex, pageSize, serviceName, serviceBid, platformPid, subSysPid, domainPid):
    result = ResultBase()

    data = {}
    pageInfo = {}
    json = {}
    if pageSize != 'None':
        pageInfo["pageSize"] = pageSize
    if pageIndex != 'None':
        pageInfo["pageIndex"] = pageIndex
    if serviceName != 'None':
        data["serviceName"] = serviceName
    if pageIndex != 'None':
        data["serviceBid"] = serviceBid
    if platformPid != 'None':
        data["platformPid"] = platformPid
    if subSysPid != 'None':
        data["subSysPid"] = subSysPid
    if domainPid != 'None':
        data["domainPid"] = domainPid

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.getMetaServiceList(json=json, headers=headers)
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


def addOrUpdateMetaService(id, serviceBid, subSysPid, serviceName, description):


    result = ResultBase()

    data = {}
    json = {}

    if id != 'None':
        data["id"] = id
    if serviceBid != 'None':
        data["serviceBid"] = serviceBid
    if subSysPid != 'None':
        data["subSysPid"] = subSysPid
    if serviceName != 'None':
        data["serviceName"] = serviceName
    if description != 'None':
        data["description"] = description

    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.addOrUpdateMetaService(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def batchUpdateField(ids, isDeleted):
    result = ResultBase()

    data = {}
    json = {}
    # idList = ids.split(',')

    if ids != 'None':
        data["ids"] = ids
    if isDeleted != 'None':
        data["isDeleted"] = isDeleted

    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.batchUpdateField(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def getInterfaceList(pageIndex, pageSize, serviceInterfaceType, interfaceName, interfaceBid, status, servicePid,
                     fieldProperty, category):
    result = ResultBase()

    data = {}
    json = {}
    pageInfo = {}

    if pageIndex != 'None':
        pageInfo["pageIndex"] = pageIndex
    if pageSize != 'None':
        pageInfo["pageSize"] = pageSize
    if serviceInterfaceType != 'None':
        data["serviceInterfaceType"] = serviceInterfaceType
    if interfaceName != 'None':
        data["interfaceName"] = interfaceName
    if interfaceBid != 'None':
        data["interfaceBid"] = interfaceBid
    if status != 'None':
        data["status"] = status
    if servicePid != 'None':
        data["servicePid"] = servicePid
    if fieldProperty != 'None':
        data["fieldProperty"] = fieldProperty
    if category != 'None':
        data["category"] = category

    json["data"] = data
    json["pageInfo"] = pageInfo

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.getInterfaceList(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def updateInterfaceStatus(id=None):
    result = ResultBase()

    headers = http_config.param_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.updateInterfaceStatus(id, headers=headers)
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


def getHexId(servicePid, serviceInterfaceType, subSysPid, fieldProperty, sign):
    result = ResultBase()
    json = {}
    data = {}

    if servicePid != 'None':
        data["servicePid"] = servicePid
    if serviceInterfaceType != 'None':
        data["serviceInterfaceType"] = serviceInterfaceType
    if subSysPid != 'None':
        data["subSysPid"] = subSysPid
    if fieldProperty != 'None':
        data["fieldProperty"] = fieldProperty
    if sign != 'None':
        data["sign"] = sign

    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.getHexId(json=json, headers=headers)
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


def batchUpdateInterfaceField(ids, isDeleted):
    result = ResultBase()

    data = {}
    json = {}
    # idList = ids.split(',')

    if ids != 'None':
        data["ids"] = ids
    if isDeleted != 'None':
        data["isDeleted"] = isDeleted

    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.batchUpdateInterfaceField(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def addOrUpdateInterface(rr_servicePid, rr_serviceInterfaceType, rr_interfaceName,
                         rr_interfaceBid, rr_interfaceDescription, rr_status,
                         list, servicePid,
                         serviceInterfaceType):
    result = ResultBase()
    data = {}
    json = {}
    rrAndffInterfaceVo = {}

    # if len(listData) > 0:
    #     list.serviceInterfaceSubelement= listData[0]
    #     list.parameterDescription = listData[1]
    #     list.dataTypeId = listData[2]
    #     list.parameterDirection = listData[3]

    # list_serviceInterfaceSubelement, list_parameterDirection,list_parameterDescription, list_dataTypeId
    # listData["serviceInterfaceSubelement"] = listData[index]
    # listData["parameterDescription"] = listData[index]
    # listData["serviceInterfaceSubelement"] = listData[index]
    # listData["parameterDescription"] = listData[index]
    # list.append(listData)

    # rrAndffInterfaceVo数据
    if rr_servicePid != 'None':
        rrAndffInterfaceVo["servicePid"] = rr_servicePid
    if rr_serviceInterfaceType != 'None':
        rrAndffInterfaceVo["serviceInterfaceType"] = rr_serviceInterfaceType
    if rr_interfaceName != 'None':
        rrAndffInterfaceVo["interfaceName"] = rr_interfaceName
    if rr_interfaceBid != 'None':
        rrAndffInterfaceVo["interfaceBid"] = rr_interfaceBid
    if rr_interfaceDescription != 'None':
        rrAndffInterfaceVo["interfaceDescription"] = rr_interfaceDescription
    if rr_status != 'None':
        rrAndffInterfaceVo["status"] = rr_status
    # List数据
    # if list_serviceInterfaceSubelement != 'None':
    #     listData["serviceInterfaceSubelement"] = list_serviceInterfaceSubelement
    # if list_parameterDescription != 'None':
    #     listData["parameterDescription"] = list_parameterDescription
    # if list_dataTypeId != 'None':
    #     listData["dataTypeId"] = list_dataTypeId
    # if list_parameterDirection != 'None':
    #     listData["parameterDirection"] = list_parameterDirection

    if len(list) > 0:
        rrAndffInterfaceVo["list"] = list

    # servicePid, serviceInterfaceType
    if servicePid != 'None':
        data["servicePid"] = servicePid
    if serviceInterfaceType != 'None':
        data["serviceInterfaceType"] = serviceInterfaceType

    data["rrAndffInterfaceVo"] = rrAndffInterfaceVo
    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.addOrUpdateInterface(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def field_addOrUpdateInterface(servicePid, serviceInterfaceType, fieldInterfaceList):
    result = ResultBase()
    data = {}
    json = {}
    # rrAndffInterfaceVo数据

    if len(fieldInterfaceList) > 0:
        data["fieldInterfaceList"] = fieldInterfaceList

    # servicePid, serviceInterfaceType
    if servicePid != 'None':
        data["servicePid"] = servicePid
    if serviceInterfaceType != 'None':
        data["serviceInterfaceType"] = serviceInterfaceType
    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.field_addOrUpdateInterface(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def event_addOrUpdateInterface(event_servicePid, event_serviceInterfaceType, event_interfaceName,
                               event_interfaceBid, event_interfaceDescription, event_status,
                               event_eventGroupPid, event_eventGroupBid, event_sendStrategy,
                               event_dataTypeId, servicePid, serviceInterfaceType):
    result = ResultBase()
    data = {}
    json = {}
    eventInterfaceVo = {}
    # rrAndffInterfaceVo数据
    # servicePid, serviceInterfaceType
    if servicePid != 'None':
        data["servicePid"] = servicePid
    if serviceInterfaceType != 'None':
        data["serviceInterfaceType"] = serviceInterfaceType
    if event_servicePid != 'None':
        eventInterfaceVo["servicePid"] = event_servicePid
    if event_serviceInterfaceType != 'None':
        eventInterfaceVo["serviceInterfaceType"] = event_serviceInterfaceType
    if event_interfaceName != 'None':
        eventInterfaceVo["interfaceName"] = event_interfaceName
    if event_interfaceBid != 'None':
        eventInterfaceVo["interfaceBid"] = event_interfaceBid
    if event_interfaceDescription != 'None':
        eventInterfaceVo["interfaceDescription"] = event_interfaceDescription
    if event_status != 'None':
        eventInterfaceVo["status"] = event_status
    if event_eventGroupPid != 'None':
        eventInterfaceVo["eventGroupPid"] = event_eventGroupPid
    if event_eventGroupBid != 'None':
        eventInterfaceVo["eventGroupBid"] = event_eventGroupBid
    if event_sendStrategy != 'None':
        eventInterfaceVo["sendStrategy"] = event_sendStrategy
    if event_dataTypeId != 'None':
        eventInterfaceVo["dataTypeId"] = event_dataTypeId

    data["eventInterfaceVo"] = eventInterfaceVo
    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.event_addOrUpdateInterface(json=json, headers=headers)
    result.success = False
    if res.status_code == 200:
        result.code = res.json()["code"]
        if res.json()["code"] == 0:
            result.success = True
            # result.msg = res.json()["result"]
        else:
            result.error = res.json()["msg"]
        result.response = res
        logger.info("分页查询列表数据 ==>> 返回结果 ==>> {}".format(result.response.text))
    else:
        result.code = res.status_code
        result.error = "请求错误"
    return result


def getInterfaceDetail(id=None):
    result = ResultBase()

    headers = http_config.param_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.getInterfaceDetail(id, headers=headers)
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


def updateInterfaceCategory(interfacePid, category, type):
    result = ResultBase()

    data = {}
    json = {}

    if interfacePid != 'None':
        data["interfacePid"] = interfacePid
    if category != 'None':
        data["category"] = category
    if type != 'None':
        data["type"] = type

    json["data"] = data

    headers = http_config.json_header

    headers["cookie"] = http_config.cookie_value
    headers["token"] = http_config.token
    # 调用api接口中的地址
    res = services.updateInterfaceCategory(json=json, headers=headers)
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
